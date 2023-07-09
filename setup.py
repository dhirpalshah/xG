from setuptools import setup

requirements = open("requirements.txt").readlines()
requirements = [r.strip() for r in requirements]

setup(
    name='xG',
    version='1.0',
    # packages=['xG_package'],
    install_requires=requirements
)