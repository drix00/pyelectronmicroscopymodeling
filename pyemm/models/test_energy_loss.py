#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2009 Hendrix Demers"
__license__ = ""

# Standard library modules.
import unittest

# Third party modules.

# Local modules.
import pyemm.models.energy_loss

# Globals and constants variables.

class TestEnergyLoss(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the testcase is working.")
        self.assert_(True)

if __name__ == '__main__':    #pragma: no cover
    import nose
    import sys
    argv = sys.argv
    argv.append("--cover-package=pyemm.models.energy_loss")
    nose.runmodule(argv=argv)
