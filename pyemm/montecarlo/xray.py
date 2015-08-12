#!/usr/bin/env python
"""
.. py:currentmodule:: montecarlo.xray
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Module for the definition of an x-ray.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Apr 14, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.

# Third party modules.
import xraylib

# Local modules.

# Project modules

# Globals and constants variables.

class CharacteristicXRay(object):
    def __init__(self, atomic_number, line, position=(0, 0, 1), direction=(0, 0, 1)):
        self.atomic_number = atomic_number
        self.line = line
        self.line_energy_keV = xraylib.LineEnergy(self.atomic_number, self.line)
        self.position = position
        self.direction = direction

    @property
    def atomic_number(self):
        return self._atomic_number
    @atomic_number.setter
    def atomic_number(self, atomic_number):
        self._atomic_number = atomic_number

    @property
    def line(self):
        return self._line
    @line.setter
    def line(self, line):
        self._line = line

    @property
    def line_energy_keV(self):
        return self._line_energy_keV
    @line_energy_keV.setter
    def line_energy_keV(self, line_energy_keV):
        self._line_energy_keV = line_energy_keV

    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, position):
        self._position = position

    @property
    def direction(self):
        return self._direction
    @direction.setter
    def direction(self, direction):
        self._direction = direction
