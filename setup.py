from setuptools import setup, find_packages

setup(
    name="notsofastapi",
    version="0.1.0",
    description="A lightweight rate-limiting library for FastAPI",
    author="apoysus",
    url="https://github.com/apoysus/notsofastapi",
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)