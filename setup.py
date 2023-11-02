# -*- coding: utf-8 -*-
"""
A brief comment just to modify the file
@author: mariodominguezf
"""

from setuptools import setup, find_packages
from entregas_machinelearning import __author__,__version__,__name__


VERSION = __version__
AUTHOR = __author__
NAME = __name__

setup(
    name                    = NAME,
    version                 = VERSION,
    description             = 'Brief description of your package',
    author                  = AUTHOR,
    author_email            = 'dominguezferrermario@gmail.com',
    license                 = 'MIT',
    python_requires         = '>=3.9.5',
    packages                = find_packages(),
    include_package_data    = True,
    package_data            = {'': ['resources/*.csv','resources/clusters/*.csv']},
    install_requires        = [
                                'pandas',
                                'numpy',
                                'torch'
                                ]
     )