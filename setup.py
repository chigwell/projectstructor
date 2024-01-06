from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ProjectStructoR',
    version='0.0.8',
    description='A tool for detecting project structure and technology stack with the help of GPT.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    url='https://github.com/chigwell/projectstructor',
    packages=find_packages(),
    install_requires=[
        'requests',
        'openai',
        'lngdetector',
        'prettytable',
        'python-magic',
        'pathspec',
        'gptintegration==0.0.3',
    ],
)
