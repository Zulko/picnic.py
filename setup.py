import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(name='picnic',
      version='0.0.0.2',
      author='Zulko 2013',
     description='Module for easy python modules creation',
     long_description=open('README.rst').read(),
     license='LICENSE.txt',
     keywords="python module template engine setuptools",
     scripts=['picnic/picnic.py'],
     packages= find_packages(exclude='docs'))	
