from setuptools import find_packages, setup

# Read in the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    
setup(
	name='chatbot_webapp',
    version="1.0",
	packages=find_packages(),
    install_requires=requirements,
)