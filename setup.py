import os
from setuptools import setup, find_packages

# Read requirements.txt file
with open('requirements.txt') as f:
	required = f.read().splitlines()

setup(
	 name='TW Biblioteca',
	 version='1.0',
	 long_description=__doc__,
	 packages=find_packages(),
	 include_package_data=True,
	 zip_safe=False,
	 install_requires=required
)