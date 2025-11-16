#!/usr/bin/env python3
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="multi-lang",
    version="1.0.0",
    author="Votre Nom",
    author_email="votre@email.com",
    description="Un langage de programmation multilingue révolutionnaire",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/votre-username/multi-lang",
    py_modules=["multi"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Interpreters",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Natural Language :: French",
        "Natural Language :: English",
        "Natural Language :: Spanish",
        "Natural Language :: Japanese",
    ],
    python_requires=">=3.7",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "multi=multi:main",
        ],
    },
    keywords="programming-language multilingual interpreter translator",
    project_urls={
        "Bug Reports": "https://github.com/votre-username/multi-lang/issues",
        "Source": "https://github.com/votre-username/multi-lang",
        "Documentation": "https://github.com/votre-username/multi-lang/wiki",
    },
)