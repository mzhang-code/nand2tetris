#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import sys 
from setuptools import setup 
from setuptools.command.test import test as TestCommand 

class PyTest(TestCommand): 
    '''pytest's integration with setuptools, which is borrowed from  
    http://pytest.org/latest/goodpractises.html#goodpractises
    '''

    def finalize_options(self): 
        TestCommand.finalize_options(self)
        self.test_args = ['-vv'] 
        # self.test_args = ['-vv', '-s'] 
        self.test_suite = True 

    def run_tests(self): 
        import pytest 
        errcode = pytest.main(self.test_args) 
        sys.exit(errcode) 

setup(
    name           = 'jcompiler', 
    version        = '0.0.1', 
    author         = 'Mengyu Zhang', 
    packages       = ['jcompiler', 'test'], 
    tests_require  = ['pytest'], 
    entry_points   = {'console_scripts': ['jcompiler = jcompiler.cli:main']}, 
    cmdclass       = {'test': PyTest}, 
    test_suite     = 'test', 
    extras_require = {'testing': ['pytest']} 
)

