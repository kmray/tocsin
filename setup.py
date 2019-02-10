import os
from setuptools import setup, find_packages
import versioneer


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="tocsin",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Keith Ray",
    author_email="keith@nullify.org",
    packages=find_packages(exclude=['tests']),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Planning"
    ],
)
