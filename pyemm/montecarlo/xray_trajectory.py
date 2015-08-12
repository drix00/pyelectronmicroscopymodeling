#!/usr/bin/env python
"""
.. py:currentmodule:: montecarlo.xray_trajectory
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
from pyemm.montecarlo.xray_event import XrayEvent

# Globals and constants variables.

class XrayTrajectory(object):
    def __init__(self, xray_id):
        self._id = xray_id
        self._events = []

    def computeFirstEvent(self, xray):
        position = xray.position
        direction = xray.direction
        energy = xray.line_energy_keV

        event = XrayEvent(position, direction, energy)
        self._events.append(event)

    def getLastEvent(self):
        return self._events[-1]

    def getLastPosition_nm(self):
        return self.getLastEvent().getPosition_nm()

    def getLastDirection(self):
        return self.getLastEvent().getDirection()

    def getLastEnergy_eV(self):
        return self.getLastEvent().getEnergy_eV()

    def addEvent(self, event):
        self._events.append(event)
