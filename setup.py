import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(name='picnic',
      version='0.0.0.4',
      author='Zulko 2014',
     description='Python packages creation made easy',
     long_description=open('README.rst').read(),
     license='see LICENSE.txt',
     keywords="python module package template engine setuptools",
     scripts=['picnic/picnic.py'],
     packages= find_packages(exclude='docs'))	
