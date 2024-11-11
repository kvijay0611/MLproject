from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT= "-e ."
def get_requirements(file_path:str)-> List[str]:
    '''
    this function will return the list of requirements 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name= 'mlproject',
version= '2.1.0',
author='keerti',
author_email='keertivijayananth06@gmail.com',
 packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",  # Replace with actual dependencies
        "pandas>=1.3.0"
    ],


)