from setuptools import setup, find_packages
from typing import List

REQUIREMENTS_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."

#declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Suvash Sharma"
DESCRIPTION = "This is my full end to end machine learning project"

def get_requirements_list()->List[str]:
    """
    Description: This function returns the contents of the file requirements.txt
    It is a list of libraries mentioned in requirements.txt.

    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list=requirement_file.readlines()       
        requirement_list=[requirement_name.replace("\n","") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)       
        return (requirement_list)
 


# #18th june 1:04


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages = find_packages(),
    install_requires=get_requirements_list()
)