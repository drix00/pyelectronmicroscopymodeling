#!/usr/bin/env python
"""
.. py:currentmodule:: annular_sdd
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Modeling of the McGill annular SDD.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Apr 14, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.
import logging

# Third party modules.
from xraylib import KL3_LINE

# Local modules.

# Project modules
from pyemm.montecarlo.xray_engine import create_xray_detector
from pyemm.montecarlo.xray import CharacteristicXRay

# Globals and constants variables.

def run():
    number_photons = 200
    xray_atomic_numbers = [5, 6, 7, 8, 14]

    for xray_atomic_numbers in xray_atomic_numbers:
        logging.info("Simulating %i", xray_atomic_numbers)
        engine = create_xray_detector()

        for photon_ID in range(number_photons):
            logging.info("photon ID %i", photon_ID)
            xray = CharacteristicXRay(xray_atomic_numbers, KL3_LINE, direction=(0, 0, -1))
            engine.simulate(xray)

        print("Backscattered: %.4f" % engine.getBackscatteredCoefficient())
        print("Absorbed:      %.4f" % engine.getAbsorbedCoefficient())
        print("Transmitted:   %.4f" % engine.getTranmittedCoefficient())

if __name__ == '__main__':  #pragma: no cover
    run()