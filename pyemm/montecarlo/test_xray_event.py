#!/usr/bin/env python
"""
.. py:currentmodule:: montecarlo.test_xray_event
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module `xray_event`.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Apr 14, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.
import unittest

# Third party modules.

# Local modules.

# Project modules
import pyemm.montecarlo.xray_event

# Globals and constants variables.

class Testxray_event(unittest.TestCase):
    """
    TestCase class for the module `xray_event`.
    """

    def setUp(self):
        """
        Setup method.
        """

        unittest.TestCase.setUp(self)

    def tearDown(self):
        """
        Teardown method.
        """

        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        """
        First test to check if the testcase is working with the testing framework.
        """

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose
    import sys
    argv = sys.argv
    argv.append("--cover-package=pyemm.montecarlo.xray_event")
    nose.runmodule(argv=argv)
