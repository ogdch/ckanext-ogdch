from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(
    name='ckanext-ogdch',
    version=version,
    description="CKAN extension for OGD portal of Switzerland",
    long_description="""\
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Liip AG',
    author_email='ogd@liip.ch',
    url='http://www.liip.ch',
    license='GPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=\
    """
    [ckan.plugins]
    ogdch=ckanext.ogdch.plugins:OgdchTheme
    """,
)
