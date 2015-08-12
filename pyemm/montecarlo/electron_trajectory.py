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
import pyemm.montecarlo.electron_event as ElectronEvent

# Globals and constants variables.

class ElectronTrajectory(object):
    def __init__(self, idElectron):
        self._idElectron = idElectron
        self._events = []

    def computeFirstEvent(self, source):
        position_nm = source.getInitialPosition_nm()
        direction = source.getInitialDirection()
        energy_eV = source.getInitialEnergy_eV()

        event = ElectronEvent.ElectronEvent(position_nm, direction, energy_eV)
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
