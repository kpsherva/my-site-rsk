# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Invenio digital library framework."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('my_site', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

invenio_db_version = ">=1.0.4,<1.1.0"
invenio_search_version = "1.3.0,<1.4.0"

extras_require = {
    "docs": ["Sphinx>=1.5.1"],
    "lorem": ["lorem>=0.1.1 "],
    "elasticsearch7": [
        "invenio-search[elasticsearch7]>={}".format(invenio_search_version),
    ],
    "postgresql": [
        "invenio-db[postgresql,versioning]{}".format(invenio_db_version),
    ],
    "mysql": [
        "invenio-db[mysql,versioning]{}".format(invenio_db_version),
    ],
    "sqlite": [
        "invenio-db[versioning]{}".format(invenio_db_version),
    ],
    "vocabulary": [
        "pycountry>=19.8.18",
    ],
}

extras_require["all"] = []
for name, reqs in extras_require.items():
    if name in (
        "mysql",
        "posgresql",
        "sqlite",
        "elasticsearch6",
        "elasticsearch7",
        "vocabulary",
    ):
        continue
    extras_require["all"].extend(reqs)


install_requires = [
    "Babel>=2.4.0",
    "Flask-BabelEx>=0.9.3",
    "invenio[base, auth, metadata, files, postgresql, elasticsearch7]>=3.2.0,<3.3.0",
    "lxml>=3.5.0,<4.2.6",
    "marshmallow>=3.0.0,<4.0.0",
    "uwsgi>=2.0",
    "uwsgi-tools>=1.1.1",
    "uwsgitop>=0.11",

    "check-manifest>=0.35",
    "coverage>=4.4.1",
    "Flask-Debugtoolbar>=0.10.1",
    "isort>=4.3",
    "mock>=2.0.0",
    "pydocstyle>=2.0.0",
    "pytest>=3.3.1",
    "pytest-cov>=2.5.1",
    "pytest-invenio>=1.2.1,<1.3.0",
    "pytest-mock>=1.6.0",
    "pytest-pep8>=1.0.6",
    "pytest-random-order>=0.5.4",
    "pytest-runner>=3.0.0,<5",
    "Sphinx>=1.5.1",

]

setup(
    name='my-site',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='my-site Invenio',
    license='MIT',
    author='CERN',
    author_email='info@my-site.com',
    url='https://github.com/my-site/my-site',
    packages=packages,
    # install_requires=install_requires,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'my-site = invenio_app.cli:cli',
        ],
        'invenio_base.apps': [
            'my_site_records = my_site.records:Mysite',
        ],
        'invenio_base.blueprints': [
            'my_site = my_site.theme.views:blueprint',
            'my_site_records = my_site.records.views:blueprint',
        ],
        'invenio_assets.webpack': [
            'my_site_theme = my_site.theme.webpack:theme',
        ],
        'invenio_config.module': [
            'my_site = my_site.config',
        ],
        'invenio_i18n.translations': [
            'messages = my_site',
        ],
        'invenio_base.api_apps': [
            'my_site = my_site.records:Mysite',
        ],
        'invenio_jsonschemas.schemas': [
            'my_site = my_site.records.jsonschemas'
        ],
        'invenio_search.mappings': [
            'records = my_site.records.mappings'
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
