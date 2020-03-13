# Describe the project and the files that belong to it. 

from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(), # tells python what package directories to include. find does it automatically
    include_package_data=True, # includes other fiels such as static and template directories
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)