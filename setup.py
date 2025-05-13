#!/usr/bin/env python3

import os
import platform
from packaging import version as V
from setuptools import setup, find_namespace_packages

install_requires = [
    "uv",  # for Python package management
    "uv-publish",  # for replacing twine to deal with ~/.pypirc until the community settles
    "packaging",  # for comparing versions
]

VERSION_FILE = os.path.join(os.path.dirname(__file__), "VERSION.txt")

setup(
    name="mtuv",
    description="Wrapper for Python packaging tooling uv and uv-publish",
    author=["Minh-Tri Pham"],
    packages=find_namespace_packages(include=["mt.*"]),
    scripts=[
        "scripts/pipi",
    ],
    install_requires=install_requires,
    python_requires=">=3.6",  # we still need to support TX2 modules coming with JetPack 4
    url="https://github.com/inteplus/mtuv",
    project_urls={
        "Documentation": "https://mtdoc.readthedocs.io/en/latest/mt.uv/mt.uv.html",
        "Source Code": "https://github.com/inteplus/mtuv",
    },
    setup_requires=["setuptools-git-versioning<2"],
    setuptools_git_versioning={
        "enabled": True,
        "version_file": VERSION_FILE,
        "count_commits_from_version_file": True,
        "template": "{tag}",
        "dev_template": "{tag}.dev{ccount}+{branch}",
        "dirty_template": "{tag}.post{ccount}",
    },
    license="MIT",
    license_files=["LICENSE"],
)
