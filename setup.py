from setuptools import setup, find_packages

setup(
    name='minbit',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        minbit=src.cli.cli:cli
    ''',
)