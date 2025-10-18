from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements =  f.read().splitlines()

setup(
    name = "Gun_Detection",
    author = "Meet_Wadekar",
    version = "1.0",
    packages = find_packages(),
    install_requires = requirements,
    )
