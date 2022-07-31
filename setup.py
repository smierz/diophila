from setuptools import setup

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="diophila",
    packages=["diophila"],
    version="0.4.0",
    author="Sandra Mierz",
    description="Python API Wrapper for OpenAlex",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="BSD-3",
    url="https://github.com/smierz/diophila",
    project_urls={
        "Bug Tracker": "https://github.com/smierz/diophila/issues",
    },
    install_requires=["requests>=2.7.0"],
    keywords=["openalex"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
    ]
)
