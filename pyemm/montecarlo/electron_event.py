#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2011 Hendrix Demers"
__license__ = ""

# Standard library modules.

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.

class ElectronEvent(object):
    def __init__(self, position_nm, direction, energy_eV):
        self._position_nm = position_nm
        self._direction = direction
        self._energy_eV = energy_eV

    def getPosition_nm(self):
        return self._position_nm

    def getDirection(self):
        return self._direction

    def getEnergy_eV(self):
        return self._energy_eV
