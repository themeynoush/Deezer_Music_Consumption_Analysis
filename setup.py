from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements, excluding -e lines.
    '''
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            line = line.strip()
            if not line.startswith('-e'):
                requirements.append(line)

    return requirements

setup(
    name='Deezer_Music_Consumption_Analysis',
    version='0.0.1',
    author='Zohreh (Meynoush) KOHANDANI',
    author_email='themeynoush@gmail.com',
    packages=find_packages(),
    # use get_requirements function for getting the requirements from requirements.txt
    install_requires=get_requirements('requirements.txt')
)
