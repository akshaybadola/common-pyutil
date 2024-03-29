import os
from setuptools import setup

from common_pyutil import __version__

description = """Some common python utility functions."""

with open("README.md") as f:
    long_description = f.read()

setup(
    name="common_pyutil",
    version=__version__,
    description=description,
    long_description=long_description,
    url="https://github.com/akshaybadola/common-pyutil",
    author="Akshay Badola",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Natural Language :: English",
    ],
    packages=["common_pyutil"],
    include_package_data=True,
    package_data={"common_pyutil": ["py.typed"]},
    keywords='utilities functional',
    python_requires=">=3.7, <=4.0",
    install_requires=["requests>=2.26.0", "file-magic>=0.4.0"]
)
