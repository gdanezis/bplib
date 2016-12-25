#!/usr/bin/env python

from setuptools import setup

import bplib

setup(name='bplib',
      # version=petlib.VERSION,
      # description='A library implementing a number of Privacy Enhancing Technologies (PETs)',
      author='George Danezis',
      author_email='g.danezis@ucl.ac.uk',
      url=r'https://pypi.python.org/pypi/bplib/',
      packages=['bplib'],
      license="LGPL",
      #long_description="""A library wrapping Open SSL low-level cryptographic libraries to build Privacy Enhancing Technoloies (PETs)""",

      setup_requires=["cffi>=1.0.0",
                      "pytest >= 2.6.4",
                      "petlib >= 0.0.30"],
      package_data = {
            "bplib": ["include/*.h"]},
      include_package_data = True,
      tests_require = [
            "cffi >= 1.0.0",
            "pycparser >= 2.10",
            "future >= 0.14.3",
            "pytest >= 2.5.0",
            "pytest-cov >= 1.8.1",
            "petlib >= 0.0.30"
            ],
      cffi_modules=["bplib/compile.py:_FFI"],
      install_requires=[
            "cffi >= 1.0.0",
            "pycparser >= 2.10",
            "future >= 0.14.3",
            "pytest >= 2.5.0",
            "pytest-cov >= 1.8.1",
            "msgpack-python >= 0.4.6",
            "petlib >= 0.0.30"
      ],
      zip_safe=False,
)