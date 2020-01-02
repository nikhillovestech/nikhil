from setuptools import setup, find_packages
import setuptools
import subprocess

from pip._internal import main as pipmain
import sys
import warnings
import os


if "--pyprof" in sys.argv:
    with open('requirements.txt') as f:
        required_packages = f.read().splitlines()
        pipmain(["install"] + required_packages)
    try:
        sys.argv.remove("--pyprof")
    except:
        pass
else:
    warnings.warn("Option --pyprof not specified. Not installing PyProf dependencies!")


setup(
name="required", # Replace with your own username
version="0.0.1",
author="Example Author",
author_email="author@example.com",
description="A small example package",
long_description="",
packages=["nikhil"],
keywords="nikhil",
package_dir={'nikhil': 'nikhil'},
long_description_content_type="text/markdown",
url="https://github.com/nikhillovestech/nikhil",
packages=setuptools.find_packages(),
classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
],
python_requires='>=3.6',
)
