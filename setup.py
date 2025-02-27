from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:

    '''
    this function will return the list of requirnment 
    '''
    requirements=[]
    try:
        with open(file_path, 'r') as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except IOError:
        print(f"Error: An issue occurred while reading the file at {file_path}.")
    
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='raj',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)