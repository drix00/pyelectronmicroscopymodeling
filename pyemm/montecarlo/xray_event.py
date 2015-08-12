#!/usr/bin/env python
"""
.. py:currentmodule:: montecarlo.xray_event
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

description
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Apr 14, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.

class XrayEvent(object):
    def __init__(self, position, direction, energy):
        self._position_nm = position
        self._direction = direction
        self._energy_eV = energy

    def getPosition_nm(self):
        return self._position_nm

    def getDirection(self):
        return self._direction

    def getEnergy_eV(self):
        return self._energy_eV
