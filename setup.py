from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='myna',
    version='0.1.0.dev1',

    description='A simple api-test framework',
    long_description=long_description,

    url='https://github.com/philoprove/myna',

    author='Kenny Zhang',
    author_email='sphy@foxmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
    ],

    keywords='reqests testing ',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['requests', 'colorama', 'json_schema_generator', 'jsonschema'],

    entry_points={
        'console_scripts': [
            'myna=myna.commands:main',
        ],
    },
)
