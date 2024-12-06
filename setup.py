from setuptools import setup, find_packages

setup(
    name='au_b24',
    version='0.1.0',
    author='Andrey Pshenitsyn',
    description='Green-api automatization library',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv'
    ],
)