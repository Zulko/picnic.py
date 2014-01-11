import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(name='picnic',
      version='0.0.0.1',
      author='Zulko 2013',
    description='Module for easy curves (x,y) manipulation',
    long_description=open('README.rst').read(),
    license='LICENSE.txt',
    keywords="curve manipulation matplotlib pylab experiments",
    scripts=['picnic/picnic.py'],
    packages= find_packages(exclude='docs'))	
