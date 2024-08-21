from setuptools import setup, find_packages

setup(
    name='metr',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'rich',
        'cookiecutter',
        'pydantic',
    ],
    entry_points={
        'console_scripts': [
            'metr=metr.metr_cli:cli',
        ],
    },
)