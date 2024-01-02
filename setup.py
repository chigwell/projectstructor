from setuptools import setup, find_packages

setup(
    name='ProjectStructoR',
    version='0.0.1',
    description='A tool for detecting project structure and technology stack with the help of GPT.',
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
    ],
)
