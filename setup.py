from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PyModbusScope',
    version='0.0.1',
    description='Automate ModbusScope using Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/spoorcc/pymodbusscope',
    author='spoorcc',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='modbus modbusscope',

    py_modules=["pymodbusscope"],
    install_requires=['pywinauto'],

    project_urls={
        'Bug Reports': 'https://github.com/spoorcc/pymodbusscope/issues',
        'Source': 'https://github.com/spoorcc/pymodbusscope/',
    },
)