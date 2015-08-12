#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2011 Hendrix Demers"
__license__ = ""

# Standard library modules.
import unittest

# Third party modules.

# Local modules.

# Project modules
from pyemm.beam.point_source import PointSource

# Globals and constants variables.

class TestPointSource(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_getInitialPosition_nm(self):
        positionRef_nm = (0.0, 0.0, 1.0e9)

        source = PointSource()
        position_nm = source.getInitialPosition_nm()

        self.assertTupleEqual(positionRef_nm, position_nm)

        #self.fail("Test if the testcase is working.")

    def test_getInitialDirection(self):
        directionRef = (0.0, 0.0, -1.0)

        source = PointSource()
        direction = source.getInitialDirection()

        self.assertTupleEqual(directionRef, direction)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose
    import sys
    argv = sys.argv
    argv.append("--cover-package=pyemm.beam.PointSource")
    nose.runmodule(argv=argv)
