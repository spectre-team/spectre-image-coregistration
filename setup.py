"""A setuptools based setup module for MSI data co-registration."""

from setuptools import setup, find_packages

setup(
    name='spectre-image-coregistration',
    version='0.0.0',
    description='Framework for co-registration of images',
    url='https://github.com/spectre-team/spectre-image-coregistration',
    author='Michal Wolny',
    author_email='Michal.Wolny@polsl.pl',
    classifiers=[
        # based on https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Image Recognition',
    ],
    packages=find_packages(exclude=['test']),
    # @gmrukwa: https://packaging.python.org/discussions/install-requires-vs-requirements/
    install_requires=[
        'numpy>=1.12.1',
        'opencv-python>=3.4.0.12',
        'typing>=3.6.2'
    ],
    python_requires='>=3.4',
    package_data={
    }
)
