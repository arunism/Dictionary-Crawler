import os
import wmtk
from setuptools import setup, find_packages

file_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(file_path, 'README.md'), 'r', encoding='utf-8') as file:
    long_description = file.read()

with open(os.path.join(file_path, 'requirements.txt'), 'r', encoding='utf-8') as file:
    requirements = file.read().splitlines()

setup(
    name='wmtk',
    version=wmtk.__version__,
    description='a web mining toolkit for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='web miner mining mine crawler crawl scraper scrape data extract extractor filter',
    author='Arun Ghimire',
    author_email='thearunism@gmail.com',
    maintainer='Arun Ghimire',
    maintainer_email='thearunism@gmail.com',
    url='https://github.com/arunism/wmtk',
    license='MIT',
    license_file='LICENSE',
    packages=find_packages(),
    install_requires=requirements,
)
