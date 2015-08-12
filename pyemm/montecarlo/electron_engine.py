#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2011 Hendrix Demers"
__license__ = ""

# Standard library modules.
import math
import random

# Third party modules.

# Local modules.

# Project modules
import pyemm.sample.bulk as SampleBulk
import pyemm.beam.point_source as PointSource
import pyemm.montecarlo.electron_trajectory as ElectronTrajectory
import pyemm.montecarlo.electron_event as ElectronEvent
import pyemm.models.models as Models
import pyemm.models.direction_cosine as DirectionCosine

# Globals and constants variables.
RESULTS_NUMBER_ELECTRONS = "numberElectrons"
RESULTS_NUMBER_BACKSCATTERED_ELECTRONS = "numberBackscatteredElectrons"

def createEngine():
    return MonteCarloEngine()

class MonteCarloEngine(object):
    MAXIMUM_NUMBERS_EVENTS = 100

    def __init__(self):
        self.reset()

        self._source = PointSource.PointSource()
        self._models = Models.Models()
        self._directionCosine = DirectionCosine.DirectionCosineDemers()

    def reset(self):
        self._results = {}

        self._results[RESULTS_NUMBER_ELECTRONS] = 0
        self._results[RESULTS_NUMBER_BACKSCATTERED_ELECTRONS] = 0

    def setSampleBulk(self, **kargs):
        self._sample = SampleBulk.SampleBulk(kargs)

    def setBeamEnergy_eV(self, energy_eV):
        self._energy_eV = energy_eV
        self._source.setInitialEnergy_eV(energy_eV)

    def simulate(self, numberElectrons=100):
        for idElectron in range(numberElectrons):
            self._computeTrajectory(idElectron)

    def _computeTrajectory(self, idElectron):
        trajectory = ElectronTrajectory.ElectronTrajectory(idElectron)

        trajectory.computeFirstEvent(self._source)
        self._numberEvents = 1

        self._computeFirstEventWithSample(trajectory)

        while not self._isTrajectoryFinished(trajectory):
            self._computeEventWithSample(trajectory)

        self._results[RESULTS_NUMBER_ELECTRONS] += 1

    def _computeFirstEventWithSample(self, trajectory):
        lastPosition_nm = trajectory.getLastPosition_nm()
        lastDirection = trajectory.getLastDirection()
        lastEnergy_eV = trajectory.getLastEnergy_eV()

        if self._sample.isIntersectSample(lastPosition_nm, lastDirection):
            intersectionPosition_nm = self._sample.getIntersectionPosition_nm(lastPosition_nm, lastDirection)

            event = ElectronEvent.ElectronEvent(intersectionPosition_nm, lastDirection, lastEnergy_eV)
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

        newEvent = ElectronEvent.ElectronEvent(position_nm, direction, energy_eV)
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

    def getBackscatteredElectronCoefficient(self):
        return self._computeBackscatteredElectronCoefficient()

    def _computeBackscatteredElectronCoefficient(self):
        if self._results[RESULTS_NUMBER_ELECTRONS] > 0:
            ratio = float(self._results[RESULTS_NUMBER_BACKSCATTERED_ELECTRONS])/float(self._results[RESULTS_NUMBER_ELECTRONS])
        else:
            ratio = 0.0

        return ratio
