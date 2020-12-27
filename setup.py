from setuptools import setup, find_packages
from os.path import join, dirname
import converter

setup(
    name='JPG-to-message',
    version=converter.__version__,
    packages=find_packages(),
    license='Apache License 2.0',
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts':
            ['converter = converter.Converter:converter']
        }
    
    )
