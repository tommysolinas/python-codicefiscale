#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

import os

exec(open("codicefiscale/version.py").read())

github_url = "https://github.com/fabiocaccamo"
sponsor_url = "https://github.com/sponsors/fabiocaccamo/"
twitter_url = "https://twitter.com/fabiocaccamo"
package_name = "python-codicefiscale"
package_url = "{}/{}".format(github_url, package_name)
package_issues_url = "{}/issues".format(github_url)
package_path = os.path.abspath(os.path.dirname(__file__))
long_description_file_path = os.path.join(package_path, "README.md")
long_description_content_type = "text/markdown"
long_description = ""
try:
    with open(long_description_file_path) as f:
        long_description = f.read()
except IOError:
    pass

setup(
    name=package_name,
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    include_package_data=True,
    version=__version__,
    description="python-codicefiscale is a tiny library for encode/decode Italian fiscal code - codifica/decodifica del Codice Fiscale.",
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    author="Fabio Caccamo",
    author_email="fabio.caccamo@gmail.com",
    url=package_url,
    download_url="{}/archive/{}.tar.gz".format(package_url, __version__),
    project_urls={
        "Documentation": package_url,
        "Issues": package_issues_url,
        "Funding": sponsor_url,
        "Twitter": twitter_url,
    },
    keywords=[
        "codicefiscale",
        "codice",
        "fiscale",
        "cf",
        "fiscal code",
    ],
    install_requires=[
        "python-dateutil ~= 2.8.0",
        "python-fsutil >= 0.6.0",
        "python-slugify == 5.0.2; python_version <= '2.7'",
        "python-slugify ~= 6.0.1; python_version >= '3.6'",
    ],
    tests_require=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Build Tools",
    ],
    license="MIT",
    test_suite="tests",
)
