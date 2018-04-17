"""Survey python package configuration."""

from setuptools import setup

setup(
    name='survey',
    version='0.1.0',
    packages=['survey'],
    include_package_data=True,
    install_requires=[
        'Flask==0.12.2',
    ],
)
