#!/usr/bin/env python
"""
.. py:currentmodule:: montecarlo.xray_engine
.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

xray_engine
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Apr 14, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.
import math
import random

# Third party modules.

# Local modules.

# Project modules
import pyemm.models.models as Models
import pyemm.models.direction_cosine as DirectionCosine
from pyemm.montecarlo.xray_trajectory import XrayTrajectory
from pyemm.montecarlo.xray_event import XrayEvent
from pyemm.sample.bulk import SampleFilm

# Globals and constants variables.
RESULTS_NUMBER_XRAYS = "numberXrays"
RESULTS_NUMBER_BACKSCATTERED_XRAYS = "numberBackscatteredXrays"
RESULTS_NUMBER_TRANSMITTED_XRAYS = "numberTransmittedXrays"
RESULTS_NUMBER_ABSORBED_XRAYS = "numberAbsorbedXrays"

def create_xray_detector():
    return MonteCarloEngine()

class MonteCarloEngine(object):
    MAXIMUM_NUMBERS_EVENTS = 100

    def __init__(self):
        self.reset()

        self._models = Models.Models()
        self._directionCosine = DirectionCosine.DirectionCosineDemers()

        self._sample = SampleFilm(atomicNumber=14)

    def reset(self):
        self._results = {}

        self._xray_id = 0
        self._results[RESULTS_NUMBER_XRAYS] = 0
        self._results[RESULTS_NUMBER_BACKSCATTERED_XRAYS] = 0
        self._results[RESULTS_NUMBER_TRANSMITTED_XRAYS] = 0
        self._results[RESULTS_NUMBER_ABSORBED_XRAYS] = 0

    def simulate(self, xray):
        self._xray_id += 1
        self._computeTrajectory(xray, self._xray_id)

    def _computeTrajectory(self, xray, xray_id):
        trajectory = XrayTrajectory(xray_id)

        trajectory.computeFirstEvent(xray)
        self._numberEvents = 1

        self._computeFirstEventWithSample(trajectory)

        while not self._isTrajectoryFinished(trajectory):
            self._computeEventWithSample(trajectory)

        self._results[RESULTS_NUMBER_XRAYS] += 1

    def _computeFirstEventWithSample(self, trajectory):
        lastPosition_nm = trajectory.getLastPosition_nm()
        lastDirection = trajectory.getLastDirection()
        lastEnergy_eV = trajectory.getLastEnergy_eV()

        if self._sample.isIntersectSample(lastPosition_nm, lastDirection):
            intersectionPosition_nm = self._sample.getIntersectionPosition_nm(lastPosition_nm, lastDirection)

            event = XrayEvent(intersectionPosition_nm, lastDirection, lastEnergy_eV)
            trajectory.addEvent(event)
            self._numberEvents += 1

    def _isTrajectoryFinished(self, trajectory):
        lastPosition_nm = trajectory.getLastPosition_nm()
        lastDirection = trajectory.getLastDirection()

        if self._numberEvents > self.MAXIMUM_NUMBERS_EVENTS:
            return True
        elif self._sample.hasExitedSample(lastPosition_nm, lastDirection):
            return True
        else:
            return False

    def _computeEventWithSample(self, trajectory):
        lastEvent = trajectory.getLastEvent()

        length_nm = self._computeNewLength_nm()
        energy_eV = self._computeNewEnergy_keV(lastEvent, length_nm)

        lastDirection = trajectory.getLastDirection()
        direction = self._computeNewDirection(lastDirection)

        lastPosition_nm = trajectory.getLastPosition_nm()
        position_nm = self._computeNewPosition_nm(lastPosition_nm, direction, length_nm)

        newEvent = XrayEvent(position_nm, direction, energy_eV)
        trajectory.addEvent(newEvent)
        self._numberEvents += 1

    def _computeNewLength_nm(self):
        meanFreePath_nm = 10.0
        length_nm = -meanFreePath_nm * math.log(random.random())
        return length_nm

    def _computeNewEnergy_keV(self, lastEvent, length_nm):
        dEdS_eV_nm = 5.0
        energyLoss_eV = dEdS_eV_nm * length_nm
        newEnergy_eV = lastEvent.getEnergy_eV() - energyLoss_eV
        return newEnergy_eV

    def _computeNewDirection(self, lastDirection):
        theta_rad = math.pi*random.random()
        phi_rad = 2.0*math.pi*random.random()

        newDirection = self._directionCosine.computeNewDirection(lastDirection, theta_rad, phi_rad)
        return newDirection

    def _computeNewPosition_nm(self, lastPosition_nm, direction, length_nm):
        position_nm = [0.0, 0.0, 0.0]
        for indexCoordinate in range(3):
            position_nm[indexCoordinate] = lastPosition_nm[indexCoordinate] + direction[indexCoordinate]*length_nm

        return position_nm

    def getBackscatteredCoefficient(self):
        return self._results[RESULTS_NUMBER_BACKSCATTERED_XRAYS] / self._results[RESULTS_NUMBER_XRAYS]

    def getAbsorbedCoefficient(self):
        return self._results[RESULTS_NUMBER_ABSORBED_XRAYS] / self._results[RESULTS_NUMBER_XRAYS]

    def getTranmittedCoefficient(self):
        return self._results[RESULTS_NUMBER_TRANSMITTED_XRAYS] / self._results[RESULTS_NUMBER_XRAYS]
