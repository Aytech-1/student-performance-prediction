from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements.txt file and returns a list of dependencies.
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters
        requirements = [req.strip() for req in requirements]
        # Remove editable install reference if present
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="ADEYEMI AYOBAMI SAMSON",
    author_email="adeyemiayobami273@gmail.com",
    description="A Machine Learning project to predict student performance",
    packages=find_packages(),  # automatically find all packages in src
    install_requires=get_requirements("requirements.txt"),  # install dependencies
    python_requires=">=3.10",  # specify your Python version
)
