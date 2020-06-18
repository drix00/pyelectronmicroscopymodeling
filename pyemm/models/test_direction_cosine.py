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
import math

# Third party modules.
import pytest

# Local modules.

# Project modules
from pyemm.models.direction_cosine import DirectionCosineDemers, DirectionCosineDemersS, DirectionCosineSoum, DirectionCosineDrouin, DirectionCosineJoy

# Globals and constants variables.

class TestDirectionCosine(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSkeleton(self):
        #self.fail("Test if the testcase is working.")
        self.assert_(True)

    def test_DirectionCosineDemers(self):
        """
        Tests for method `DirectionCosineDemers`.
        """

        lastDirection = (0, 0, 1)
        theta_rad = 0.0
        phi_rad = 0.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDemers()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/2.0
        phi_rad = 0.0
        direction_ref = (1.0, 0.0, 0.0)
        direction_cosine = DirectionCosineDemers()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = 0.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDemers()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/2.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 1.0, 0.0)
        direction_cosine = DirectionCosineDemers()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/4.0
        phi_rad = 0.0
        direction_ref = (0.7071067811865475, 0.0, -0.7071067811865475)
        direction_cosine = DirectionCosineDemers()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = 0.0
        phi_rad = math.pi/4.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDemers()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/4.0
        phi_rad = math.pi/4.0
        direction_ref = (0.5, 0.5, -0.707106781186547)
        direction_cosine = DirectionCosineDemers()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = 0.0
        phi_rad = 0.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDemers()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/2.0
        phi_rad = 0.0
        direction_ref = (1.0, 0.0, 0.0)
        direction_cosine = DirectionCosineDemers()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = 0.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDemers()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/2.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 1.0, 0.0)
        direction_cosine = DirectionCosineDemers()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/4.0
        phi_rad = 0.0
        direction_ref = (0.7071067811865475, 0.0, -0.7071067811865475)
        direction_cosine = DirectionCosineDemers()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = 0.0
        phi_rad = math.pi/4.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDemers()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/4.0
        phi_rad = math.pi/4.0
        direction_ref = (0.5, 0.5, -0.707106781186547)
        direction_cosine = DirectionCosineDemers()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        #self.fail("Test if the testcase is working.")

    def test_DirectionCosineDemersS(self):
        """
        Tests for method `DirectionCosineDemersS`.
        """

        lastDirection = (0, 0, 1)
        theta_rad = 0.0
        phi_rad = 0.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDemersS()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/2.0
        phi_rad = 0.0
        direction_ref = (1.0, 0.0, 0.0)
        direction_cosine = DirectionCosineDemersS()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = 0.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDemersS()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/2.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 1.0, 0.0)
        direction_cosine = DirectionCosineDemersS()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/4.0
        phi_rad = 0.0
        direction_ref = (0.7071067811865475, 0.0, -0.7071067811865475)
        direction_cosine = DirectionCosineDemersS()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = 0.0
        phi_rad = math.pi/4.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDemersS()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/4.0
        phi_rad = math.pi/4.0
        direction_ref = (0.5, 0.5, -0.707106781186547)
        direction_cosine = DirectionCosineDemersS()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = 0.0
        phi_rad = 0.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDemersS()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/2.0
        phi_rad = 0.0
        direction_ref = (1.0, 0.0, 0.0)
        direction_cosine = DirectionCosineDemersS()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = 0.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDemersS()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/2.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 1.0, 0.0)
        direction_cosine = DirectionCosineDemersS()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/4.0
        phi_rad = 0.0
        direction_ref = (0.7071067811865475, 0.0, -0.7071067811865475)
        direction_cosine = DirectionCosineDemersS()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = 0.0
        phi_rad = math.pi/4.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDemersS()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/4.0
        phi_rad = math.pi/4.0
        direction_ref = (0.5, 0.5, -0.707106781186547)
        direction_cosine = DirectionCosineDemersS()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        #self.fail("Test if the testcase is working.")

    @pytest.mark.skip("Not implemented")
    def test_DirectionCosineSoum(self):
        """
        Tests for method `DirectionCosineSoum`.
        """

        lastDirection = (0, 0, 1)
        theta_rad = 0.0
        phi_rad = 0.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineSoum()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/2.0
        phi_rad = 0.0
        direction_ref = (1.0, 0.0, 0.0)
        direction_cosine = DirectionCosineSoum()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = 0.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineSoum()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/2.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 1.0, 0.0)
        direction_cosine = DirectionCosineSoum()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/4.0
        phi_rad = 0.0
        direction_ref = (0.7071067811865475, 0.0, -0.7071067811865475)
        direction_cosine = DirectionCosineSoum()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = 0.0
        phi_rad = math.pi/4.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineSoum()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/4.0
        phi_rad = math.pi/4.0
        direction_ref = (0.5, 0.5, -0.707106781186547)
        direction_cosine = DirectionCosineSoum()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = 0.0
        phi_rad = 0.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineSoum()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/2.0
        phi_rad = 0.0
        direction_ref = (1.0, 0.0, 0.0)
        direction_cosine = DirectionCosineSoum()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = 0.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineSoum()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/2.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 1.0, 0.0)
        direction_cosine = DirectionCosineSoum()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/4.0
        phi_rad = 0.0
        direction_ref = (0.7071067811865475, 0.0, -0.7071067811865475)
        direction_cosine = DirectionCosineSoum()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = 0.0
        phi_rad = math.pi/4.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineSoum()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/4.0
        phi_rad = math.pi/4.0
        direction_ref = (0.5, 0.5, -0.707106781186547)
        direction_cosine = DirectionCosineSoum()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        self.fail("Test if the testcase is working.")

    @pytest.mark.skip("Not implemented")
    def test_DirectionCosineDrouin(self):
        """
        Tests for method `DirectionCosineDrouin`.
        """

        lastDirection = (0, 0, 1)
        theta_rad = 0.0
        phi_rad = 0.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDrouin()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/2.0
        phi_rad = 0.0
        direction_ref = (1.0, 0.0, 0.0)
        direction_cosine = DirectionCosineDrouin()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = 0.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDrouin()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/2.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 1.0, 0.0)
        direction_cosine = DirectionCosineDrouin()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/4.0
        phi_rad = 0.0
        direction_ref = (0.7071067811865475, 0.0, -0.7071067811865475)
        direction_cosine = DirectionCosineDrouin()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = 0.0
        phi_rad = math.pi/4.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDrouin()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/4.0
        phi_rad = math.pi/4.0
        direction_ref = (0.5, 0.5, -0.707106781186547)
        direction_cosine = DirectionCosineDrouin()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = 0.0
        phi_rad = 0.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDrouin()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/2.0
        phi_rad = 0.0
        direction_ref = (1.0, 0.0, 0.0)
        direction_cosine = DirectionCosineDrouin()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = 0.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDrouin()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/2.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 1.0, 0.0)
        direction_cosine = DirectionCosineDrouin()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/4.0
        phi_rad = 0.0
        direction_ref = (0.7071067811865475, 0.0, -0.7071067811865475)
        direction_cosine = DirectionCosineDrouin()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = 0.0
        phi_rad = math.pi/4.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineDrouin()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/4.0
        phi_rad = math.pi/4.0
        direction_ref = (0.5, 0.5, -0.707106781186547)
        direction_cosine = DirectionCosineDrouin()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        self.fail("Test if the testcase is working.")

    def test_DirectionCosineJoy(self):
        """
        Tests for method `DirectionCosineJoy`.
        """

        lastDirection = (0, 0, 1)
        theta_rad = 0.0
        phi_rad = 0.0
        direction_ref = (0.0, 0.0, 1.0)
        direction_cosine = DirectionCosineJoy()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/2.0
        phi_rad = 0.0
        direction_ref = (1.0, 0.0, 0.0)
        direction_cosine = DirectionCosineJoy()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = 0.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 0.0, 1.0)
        direction_cosine = DirectionCosineJoy()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/2.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 1.0, 0.0)
        direction_cosine = DirectionCosineJoy()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/4.0
        phi_rad = 0.0
        direction_ref = (0.7071067811865475, 0.0, 0.7071067811865475)
        direction_cosine = DirectionCosineJoy()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = 0.0
        phi_rad = math.pi/4.0
        direction_ref = (0.0, 0.0, 1.0)
        direction_cosine = DirectionCosineJoy()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, 1)
        theta_rad = math.pi/4.0
        phi_rad = math.pi/4.0
        direction_ref = (0.5, 0.5, 0.707106781186547)
        direction_cosine = DirectionCosineJoy()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = 0.0
        phi_rad = 0.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineJoy()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/2.0
        phi_rad = 0.0
        direction_ref = (1.0, 0.0, 0.0)
        direction_cosine = DirectionCosineJoy()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = 0.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineJoy()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/2.0
        phi_rad = math.pi/2.0
        direction_ref = (0.0, -1.0, 0.0)
        direction_cosine = DirectionCosineJoy()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/4.0
        phi_rad = 0.0
        direction_ref = (0.7071067811865475, 0.0, -0.7071067811865475)
        direction_cosine = DirectionCosineJoy()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = 0.0
        phi_rad = math.pi/4.0
        direction_ref = (0.0, 0.0, -1.0)
        direction_cosine = DirectionCosineJoy()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        lastDirection = (0, 0, -1)
        theta_rad = math.pi/4.0
        phi_rad = math.pi/4.0
        direction_ref = (0.5, -0.5, -0.707106781186547)
        direction_cosine = DirectionCosineJoy()
        new_direction = direction_cosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        self.assertAlmostEqual(direction_ref[0], new_direction[0])
        self.assertAlmostEqual(direction_ref[1], new_direction[1])
        self.assertAlmostEqual(direction_ref[2], new_direction[2])

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose
    import sys
    argv = sys.argv
    argv.append("--cover-package=pyemm.models.direction_cosine")
    nose.runmodule(argv=argv)
