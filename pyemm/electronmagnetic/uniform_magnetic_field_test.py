#!/usr/bin/env python
"""
.. py:currentmodule:: electronmagnetic.uniform_magnetic_field_test
   :synopsis: Tests for the module :py:mod:`uniform_magnetic_field`

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the module :py:mod:`uniform_magnetic_field`.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Oct 9, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.
import unittest

# Third party modules.

# Local modules.

# Project modules
from pyemm.electronmagnetic.uniform_magnetic_field import compute_velocity_nm_s, compute_relativistic_velocity_nm_s

# Globals and constants variables.

class Testuniform_magnetic_field(unittest.TestCase):
    """
    TestCase class for the module `uniform_magnetic_field`.
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
        self.assert_(True)

    def test_velocity_nm_s(self):
        """
        Test compute_velocity_nm_s method.
        """

        velocityRefs_m_s = {100: 1.644, 120: 1.759, 200: 2.086, 300: 2.330, 400: 2.484, 1000: 2.823}

        for energy_keV in velocityRefs_m_s:
            velocityRef_m_s = velocityRefs_m_s[energy_keV]

            velocity_nm_s = compute_velocity_nm_s(energy_keV)
            velocity_m_s = velocity_nm_s*1.0e-9 * 1.0e-8
            self.assertAlmostEqual(velocityRef_m_s, velocity_m_s, 4)

        self.fail("Test if the testcase is working.")

    def test_compute_relativistic_velocity_nm_s(self):
        """
        Test compute_relativistic_velocity_nm_s method.
        """

        velocityRefs_m_s = {100: 1.6435100357270491,
                            120: 1.75877975489859,
                            200: 2.0844819661337146,
                            300: 2.3279446107947876,
                            400: 2.4818673114757841,
                            1000: 2.8212609222440674}

        for energy_keV in velocityRefs_m_s:
            velocityRef_m_s = velocityRefs_m_s[energy_keV]

            velocity_nm_s = compute_relativistic_velocity_nm_s(energy_keV)
            velocity_m_s = velocity_nm_s*1.0e-9 * 1.0e-8
            self.assertAlmostEqual(velocityRef_m_s, velocity_m_s, 4)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__':  #pragma: no cover
    import nose
    import sys
    argv = sys.argv
    argv.append("--with-coverage")
    argv.append("--cover-package=pyemm.electronmagnetic.uniform_magnetic_field")
    nose.runmodule(argv=argv)
