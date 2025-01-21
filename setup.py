'''
The setup.py file is an essential part of packaging and distributing Python projects. 
It is used by setuptools (or distutils in older Python versions) to define the configurationof 
your project, such as its metadata, dependencies, and more.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements( ) -> List[str]:
    """
    This function will return list of requirements
    """
    
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            # Read lines from file
            lines = file.readlines()
            ## Process each line
            for line in lines:
                requirement = line.strip()
                ## Ignore empty lines and -e.
                if requirement and requirement != '-e':
                    requirement_lst.append(requirement)
    except FileNotFoundError:                
        print("requirements.txt file not found")
        
    return requirement_lst

setup(
    name = "Netwrok Security",
    version = "0.0.1",
    author = "Vikas Jangid",
    author_email = "vikasjangid@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)