from setuptools import setup, find_packages

requirements = open('requirements.txt','r').read()

setup(
    name="Piper",
    version="0.0.1",
    description="Remote Access Tool that uses steganography to keep it's malicious codes.",
    packages=find_packages(),
    install_requires=requirements
)