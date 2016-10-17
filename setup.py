#
# setup.py
#
"""
Setup file for Starkoala project.
"""

from setuptools import setup
from importlib.machinery import SourceFileLoader

NAME = 'starkoala'

REQUIRES = [
    'growler',
]

OPTIONAL_REQUIRES = {
}

TESTS_REQUIRE = [
    'pytest',
    'pytest-asyncio',
]

PACKAGES = [
    'starkoala',
]

SETUP_REQUIRES = [
    'pytest-runner',
]

NAMESPACES = []


CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Environment :: Web Environment",
    "Operating System :: OS Independent",
    # "Framework :: Growler",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Topic :: Internet :: WWW/HTTP",
    "Natural Language :: English",
]

metadata = SourceFileLoader("metadata", 'starkoala/__meta__.py').load_module()


setup(
    name=NAME,
    version=metadata.version,
    author=metadata.author,
    license=metadata.license,
    url=metadata.url,
    author_email=metadata.author_email,
    description=metadata.description,
    classifiers=CLASSIFIERS,
    install_requires=REQUIRES,
    extras_require=OPTIONAL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    packages=PACKAGES,
    namespace_packages=NAMESPACES,
    platforms='all',
)
