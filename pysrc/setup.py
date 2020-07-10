#!/usr/bin/env python

import os
import sys

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
desc = 'Python tools for working with the embedvm virtual machine'
long_desc = ''

setup(name='embedvm',
      author='CJ Niemira',
      author_email='siege@siege.org',
      version='0.1.0',
      description=desc,
      long_description=desc + long_desc,
      classifiers=[
          "Programming Language :: Python",
      ],
      url='',
      keywords='',
      packages=[
            'embedvm',
            ],
      include_package_data=True,
      zip_safe=False,
      setup_requires=[],
      tests_require=[],
      install_requires=[],
      entry_points="""\
      [console_scripts]
      evm-disasm = embedvm.cli.disasm:main
      evm-asm = embedvm.cli.asm:main
      evm-pycomp = embedvm.cli.comp:main
      """,
      )
