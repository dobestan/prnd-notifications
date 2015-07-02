from setuptools import setup, find_packages
from pip.req import parse_requirements

import os


requirements_generator = parse_requirements(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "requirements.txt",
    ),
    session=False,
)
requirements = [str(requirement.req) for requirement in requirements_generator]

setup(
    name="prnd-notifications",
    description="all-in-one notifications app - manage all PRND notifications including SMS, Email, Slack",
    version="0.1.0",
    author="Suchan An",
    author_email="dobestan@prnd.co.kr",
    url="https://github.com/PRNDcompany/prnd-notifications",
    packages=find_packages(),
    include_package_date=True,
    install_requires=requirements,
)
