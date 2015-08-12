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

class PointSource(object):
    def __init__(self):
        self._position_nm = (0.0, 0.0, 1.0e9)
        self._direction = (0.0, 0.0, -1.0)
        self._energy_eV = None

    def getInitialPosition_nm(self):
        return self._position_nm

    def getInitialDirection(self):
        return self._direction

    def setInitialEnergy_eV(self, energy_eV):
        self._energy_eV = energy_eV

    def getInitialEnergy_eV(self):
        return self._energy_eV
