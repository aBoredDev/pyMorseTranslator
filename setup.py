#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
      name='pyMorseTranslator',
      version='1.2.0',
      author='Robbie Munro',
      author_email='rmunro2324@gmail.com',
      packages=find_packages(),
      url='https://github.com/Eagle-Eye2324/pyMorseTranslator',
      license='GPL-3.0-only',
      description='A library for decoding and encoding strings in Morse code.',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown'
)
