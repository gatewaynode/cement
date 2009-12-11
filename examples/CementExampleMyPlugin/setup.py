from setuptools import setup, find_packages
import sys, os

version = '0.1beta'

setup(name='CementExampleMyPlugin',
    version=version,
    description="Cement Example Plugin called MyPlugin",
    long_description="""Cement Example Plugin called MyPlugin""",
    classifiers=[], 
    keywords='',
    author='BJ Dierkes',
    author_email='wdierkes@5dollarwhitebox.org',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
        ],
    entry_points="""
    [console_scripts]
    """,
    namespace_packages=['cement_example', 'cement_example.plugins'],
    )