from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List:
    """
    Project practice package
    """
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace('\n', '') for req in requirements if req!='-e .']
    return requirements


setup(
    name='Project_practice', 
    version='0.1',
    author='UMESH',
    author_email='umeshgouda143@gmail.com', 
    packages=find_packages(), 
    install_requires=get_requirements('requirements.txt')
)