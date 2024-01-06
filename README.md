[![PyPI version](https://badge.fury.io/py/ProjectStructoR.svg)](https://badge.fury.io/py/ProjectStructoR)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/projectstructor)](https://pepy.tech/project/projectstructor)

# ProjectStructoR

`ProjectStructoR` is a Python tool designed to analyze directories and detect the project structure and technology stack used in the files. It leverages GPT from OpenAI to provide a comprehensive analysis including the count of files, lines of code, and the likely technologies present.

## Installation

To install `ProjectStructoR`, you can use pip:

```bash
pip install ProjectStructoR
```

## Usage

### As a Python Module

ProjectStructoR can be used as a Python module in your scripts.

Example:

```python
from projectstructor.detector import ProjectStructureDetector

# Initialize the detector with the target directory and your OpenAI API key
detector = ProjectStructureDetector('/path/to/your/project', 'your-openai-api-key')

# Detect the structure of the project
print(detector.detect_structure(ignore_gitignore=True))

# Detect the languages used in the project
print(detector.detect_languages())

# Analyze with GPT and print the JSON result
chat_completion = detector.analyze_with_gpt()
content = chat_completion.choices[0].message.content
result = json.loads(content)
print(json.dumps(result, indent=2))
```

### As a Command Line Tool

Currently, `ProjectStructoR` is intended to be used as a module in Python scripts. If there's enough interest, command line functionality may be added in future versions.

## Output Example

When you run `ProjectStructoR`, it outputs the structure of the project directory and a report with the detected languages and technologies. Here is an example output:

```
detected structure: 
project/
|-- main.py
|-- utils/
|   |-- __init__.py
|   |-- helper.py

detected languages and technologies: 
Python files: 3, lines of code: 120
JavaScript files: 1, lines of code: 45
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/chigwell/projectstructor/issues).

## License

[MIT](https://choosealicense.com/licenses/mit/)