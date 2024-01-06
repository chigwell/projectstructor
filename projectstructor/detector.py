import os
from lngdetector.main import generate_report
from gptintegration import GPTIntegration
import pathspec

class ProjectStructureDetector:
    def __init__(self, directory, gpt_api_key, gpt_model="gpt-3.5-turbo"):
        self.directory = directory
        self.gpt_api_key = gpt_api_key
        self.gpt_model = gpt_model

    def detect_structure(self, ignore_gitignore=True):
        file_structure = ""
        gitignore_spec = None

        if ignore_gitignore:
            gitignore_path = os.path.join(self.directory, '.gitignore')
            if os.path.exists(gitignore_path):
                with open(gitignore_path, 'r') as file:
                    gitignore_spec = pathspec.PathSpec.from_lines('gitwildmatch', file)

        for root, dirs, files in os.walk(self.directory, topdown=True):
            relative_dirs = [os.path.relpath(os.path.join(root, d), self.directory) for d in dirs]
            relative_files = [os.path.relpath(os.path.join(root, f), self.directory) for f in files]

            if gitignore_spec:
                dirs[:] = [d for d in relative_dirs if not gitignore_spec.match_file(d)]
                files = [f for f in relative_files if not gitignore_spec.match_file(f)]

            for name in files:
                if len(file_structure) + len(name) < 1500:
                    file_structure += name + "\n"

        return file_structure[:1500]

    def detect_languages(self):
        report = generate_report(self.directory)
        languages_summary = []
        for language, data in report.languages.items():
            languages_summary.append(f"{language} files: {data['count']}, lines of code: {data['lines']}")
        return "; ".join(languages_summary)

    def analyze_with_gpt(self):
        system_message = "Analyze the given project file structure and language report to determine the most likely frameworks and technology stacks used, along with their versions. Please provide the response in a strict JSON format with an array of objects, each containing 'tech' for technology name, 'ver' for version, and 'probability' indicating the confidence level. The response should be concise, accurately formatted, and suitable for straightforward parsing and reuse in subsequent queries.\n\nEnsure the response adheres strictly to the following JSON structure: \n\n[{\"tech\": \"<Technology Name>\", \"ver\": \"<Version>\", \"probability\": \"<Confidence Level>\"}, ...]\n\nFor example, if you identify Django REST framework and Python with certain confidence levels, the appropriate response should look like:\n\n[{\"tech\": \"Django REST\", \"ver\": \"3.1\", \"probability\": \"0.89\"}, {\"tech\": \"Python\", \"ver\": \"3.8\", \"probability\": \"0.95\"}, ...]\n\nThis format allows for easy parsing and direct application in further processing or decision-making processes."
        user_message = "I need an analysis of the frameworks and technology stacks used in my project based on the following project file structure and language report: \n\n" + self.detect_structure() + "\n\n" + self.detect_languages() + "\n\n"

        gpt_integration = GPTIntegration(self.gpt_api_key, self.gpt_model)
        response = gpt_integration.query_gpt(system_message, [user_message])
        return response
