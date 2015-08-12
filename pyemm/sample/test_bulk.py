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
from pyemm.sample.bulk import SampleBulk

# Globals and constants variables.

class TestBulk(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_init(self):
        atomicNumberRef = 6
        sample = SampleBulk(atomicNumberRef)

        self.assertEquals(atomicNumberRef, sample._atomicNumber)

        #self.fail("Test if the testcase is working.")

    def test_isIntersectSample(self):
        atomicNumberRef = 6
        sample = SampleBulk(atomicNumberRef)

        position_nm = (0.0, 0.0, 1.0)
        direction = (0.0, 0.0, 1.0)
        self.assertFalse(sample.isIntersectSample(position_nm, direction))

        position_nm = (0.0, 0.0, 1.0)
        direction = (0.0, 0.0, -1.0)
        self.assertTrue(sample.isIntersectSample(position_nm, direction))

        position_nm = (0.0, 0.0, -1.0)
        direction = (0.0, 0.0, 1.0)
        self.assertTrue(sample.isIntersectSample(position_nm, direction))

        position_nm = (0.0, 0.0, -1.0)
        direction = (0.0, 0.0, -1.0)
        self.assertFalse(sample.isIntersectSample(position_nm, direction))

        sample = SampleBulk(atomicNumberRef)
        sample._topSurface_nm = 0.5

        position_nm = (0.0, 0.0, 1.0)
        direction = (0.0, 0.0, 1.0)
        self.assertFalse(sample.isIntersectSample(position_nm, direction))

        position_nm = (0.0, 0.0, 1.0)
        direction = (0.0, 0.0, -1.0)
        self.assertTrue(sample.isIntersectSample(position_nm, direction))

        position_nm = (0.0, 0.0, -1.0)
        direction = (0.0, 0.0, 1.0)
        self.assertTrue(sample.isIntersectSample(position_nm, direction))

        position_nm = (0.0, 0.0, -1.0)
        direction = (0.0, 0.0, -1.0)
        self.assertFalse(sample.isIntersectSample(position_nm, direction))

        position_nm = (0.0, 0.0, sample._topSurface_nm)
        direction = (0.0, 0.0, 1.0)
        self.assertFalse(sample.isIntersectSample(position_nm, direction))

        position_nm = (0.0, 0.0, sample._topSurface_nm)
        direction = (0.0, 0.0, -1.0)
        self.assertTrue(sample.isIntersectSample(position_nm, direction))

        #self.fail("Test if the testcase is working.")

    def test_getIntersectionPosition_nm(self):
        atomicNumberRef = 6
        sample = SampleBulk(atomicNumberRef)

        newPositionRef_nm = (0.0, 0.0, 0.0)

        position_nm = (0.0, 0.0, 1.0)
        direction = (0.0, 0.0, 1.0)
        self.assertRaises(ValueError, sample.getIntersectionPosition_nm, position_nm, direction)

        position_nm = (0.0, 0.0, 1.0)
        direction = (0.0, 0.0, -1.0)
        newPosition_nm = sample.getIntersectionPosition_nm(position_nm, direction)
        self.assertTupleEqual(newPositionRef_nm, newPosition_nm)

        position_nm = (0.0, 0.0, -1.0)
        direction = (0.0, 0.0, 1.0)
        newPosition_nm = sample.getIntersectionPosition_nm(position_nm, direction)
        self.assertTupleEqual(newPositionRef_nm, newPosition_nm)

        position_nm = (0.0, 0.0, -1.0)
        direction = (0.0, 0.0, -1.0)
        self.assertRaises(ValueError, sample.getIntersectionPosition_nm, position_nm, direction)

        sample = SampleBulk(atomicNumberRef)
        sample._topSurface_nm = 0.5
        newPositionRef_nm = (0.0, 0.0, sample._topSurface_nm)

        position_nm = (0.0, 0.0, 1.0)
        direction = (0.0, 0.0, 1.0)
        self.assertRaises(ValueError, sample.getIntersectionPosition_nm, position_nm, direction)

        position_nm = (0.0, 0.0, 1.0)
        direction = (0.0, 0.0, -1.0)
        newPosition_nm = sample.getIntersectionPosition_nm(position_nm, direction)
        self.assertTupleEqual(newPositionRef_nm, newPosition_nm)

        position_nm = (0.0, 0.0, -1.0)
        direction = (0.0, 0.0, 1.0)
        newPosition_nm = sample.getIntersectionPosition_nm(position_nm, direction)
        self.assertTupleEqual(newPositionRef_nm, newPosition_nm)

        position_nm = (0.0, 0.0, -1.0)
        direction = (0.0, 0.0, -1.0)
        self.assertRaises(ValueError, sample.getIntersectionPosition_nm, position_nm, direction)

        position_nm = (0.0, 0.0, sample._topSurface_nm)
        direction = (0.0, 0.0, 1.0)
        self.assertRaises(ValueError, sample.getIntersectionPosition_nm, position_nm, direction)

        position_nm = (0.0, 0.0, sample._topSurface_nm)
        direction = (0.0, 0.0, -1.0)
        newPosition_nm = sample.getIntersectionPosition_nm(position_nm, direction)
        self.assertTupleEqual(newPositionRef_nm, newPosition_nm)

        #self.fail("Test if the testcase is working.")

    def test_hasExitedSample(self):
        atomicNumberRef = 6
        sample = SampleBulk(atomicNumberRef)

        position_nm = (0.0, 0.0, 1.0)
        direction = (0.0, 0.0, 1.0)
        self.assertTrue(sample.hasExitedSample(position_nm, direction))

        position_nm = (0.0, 0.0, 1.0)
        direction = (0.0, 0.0, -1.0)
        self.assertTrue(sample.hasExitedSample(position_nm, direction))

        position_nm = (0.0, 0.0, -1.0)
        direction = (0.0, 0.0, 1.0)
        self.assertFalse(sample.hasExitedSample(position_nm, direction))

        position_nm = (0.0, 0.0, -1.0)
        direction = (0.0, 0.0, -1.0)
        self.assertFalse(sample.hasExitedSample(position_nm, direction))

        sample = SampleBulk(atomicNumberRef)
        sample._topSurface_nm = 0.5

        position_nm = (0.0, 0.0, 1.0)
        direction = (0.0, 0.0, 1.0)
        self.assertTrue(sample.hasExitedSample(position_nm, direction))

        position_nm = (0.0, 0.0, 1.0)
        direction = (0.0, 0.0, -1.0)
        self.assertTrue(sample.hasExitedSample(position_nm, direction))

        position_nm = (0.0, 0.0, -1.0)
        direction = (0.0, 0.0, 1.0)
        self.assertFalse(sample.hasExitedSample(position_nm, direction))

        position_nm = (0.0, 0.0, -1.0)
        direction = (0.0, 0.0, -1.0)
        self.assertFalse(sample.hasExitedSample(position_nm, direction))

        position_nm = (0.0, 0.0, sample._topSurface_nm)
        direction = (0.0, 0.0, 1.0)
        self.assertFalse(sample.hasExitedSample(position_nm, direction))

        position_nm = (0.0, 0.0, sample._topSurface_nm)
        direction = (0.0, 0.0, -1.0)
        self.assertFalse(sample.hasExitedSample(position_nm, direction))

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose
    import sys
    argv = sys.argv
    argv.append("--cover-package=pyemm.sample.bulk")
    nose.runmodule(argv=argv)
