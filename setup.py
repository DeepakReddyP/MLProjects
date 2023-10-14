from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirments(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name='MLProjects',
version='0.0.1',
author='Pujari Deepak Reddy',
author_email='pujarideepakreddy.y@gmail.com',
packages=find_packages(),
install_requires=get_requirments('requirements.txt')
)