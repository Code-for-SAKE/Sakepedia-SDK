# Author: Code for SAKE
# Copyright (c) 2022 Code for SAKE
# License: MIT License

from setuptools import setup
import sakepedia

DESCRIPTION = "sakepedia: Sakepedia API"
NAME = 'sakepedia'
AUTHOR = 'Code for SAKE'
URL = 'https://www.code4sake.org/'
LICENSE = 'MIT License'
DOWNLOAD_URL = 'https://github.com/Code-for-SAKE/SakepediaSDK'
VERSION = sakepedia.__version__
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
    'urllib3>=1.24.3',
    'jsonschema>=4.3.3',
    'bs4>=0.0.1',
]

EXTRAS_REQUIRE = {
}

PACKAGES = [
    'sakepedia'
]

CLASSIFIERS = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
]

with open('README.md', 'r') as fp:
    readme = fp.read()
long_description = readme

setup(name=NAME,
      author=AUTHOR,
      maintainer=AUTHOR,
      description=DESCRIPTION,
      long_description=long_description,
      long_description_content_type="text/markdown",
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE,
      packages=PACKAGES,
      classifiers=CLASSIFIERS
    )