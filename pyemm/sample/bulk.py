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
X = 0
Y = 1
Z = 2

class SampleBulk(object):
    def __init__(self, atomicNumber):
        self._atomicNumber = atomicNumber

        self._create()

    def _create(self):
        self._topSurface_nm = 0.0

    def isIntersectSample(self, position_nm, direction):
        if direction[Z] > 0.0 and position_nm[Z] < self._topSurface_nm:
            return True
        elif direction[Z] < 0.0 and position_nm[Z] >= self._topSurface_nm:
            return True

        return False

    def getIntersectionPosition_nm(self, position_nm, direction):
        if self.isIntersectSample(position_nm, direction):
            newPosition = (position_nm[X], position_nm[Y], self._topSurface_nm)

            if direction[Z] > 0.0 and position_nm[Z] < self._topSurface_nm:
                return newPosition
            elif direction[Z] < 0.0 and position_nm[Z] >= self._topSurface_nm:
                return newPosition
        else:
            message = "Position and direction does not intersect the sample."
            raise ValueError(message)

    def hasExitedSample(self, position_nm, direction):
        if position_nm[Z] > self._topSurface_nm:
            return True
        else:
            return False

class SampleFilm(object):
    def __init__(self, atomicNumber, thickness_cm=0.045):
        self._atomicNumber = atomicNumber
        self._thickness_cm = thickness_cm

        self._create()

    def _create(self):
        self._topSurface_nm = 0.0
        self._bottom_surface_nm = self._thickness_cm

    def isIntersectSample(self, position_nm, direction):
        if direction[Z] > 0.0 and position_nm[Z] < self._topSurface_nm:
            return True
        elif direction[Z] < 0.0 and position_nm[Z] >= self._topSurface_nm:
            return True

        return False

    def getIntersectionPosition_nm(self, position_nm, direction):
        if self.isIntersectSample(position_nm, direction):
            newPosition = (position_nm[X], position_nm[Y], self._topSurface_nm)

            if direction[Z] > 0.0 and position_nm[Z] < self._topSurface_nm:
                return newPosition
            elif direction[Z] < 0.0 and position_nm[Z] >= self._topSurface_nm:
                return newPosition
        else:
            message = "Position and direction does not intersect the sample."
            raise ValueError(message)

    def hasExitedSample(self, position_nm, direction):
        if position_nm[Z] > self._topSurface_nm:
            return True
        else:
            return False
