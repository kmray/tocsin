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
    url="https://github.com/kmray/tocsin",
    packages=find_packages(exclude=['tests']),
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Home Automation"
    ],
    install_requires=[]
)
