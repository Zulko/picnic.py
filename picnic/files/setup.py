import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(name='$PACKAGE_NAME',
      version='0.1.0',
      author='$AUTHOR',
    description='',
    long_description=open('README.rst').read(),
    license='see LICENSE.txt',
    keywords="",
    packages= find_packages(exclude='docs'))
