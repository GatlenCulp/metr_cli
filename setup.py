from setuptools import setup, find_packages

setup(
    name='metr-cli',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'cookiecutter',
        'docker',
    ],
    entry_points={
        'console_scripts': [
            'metr=src.cli:cli',
        ],
    },
)