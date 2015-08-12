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

# Third party modules.

# Local modules.

# Project modules

# Globals and constants variables.

class DirectionCosine(object):
    def __init__(self, polarAngleInitial_rad=0.0, azimuthalAngleInitial_rad=0.0):
        """
        param[in] polarAngleInitial_rad
        param[in] azimuthalAngleInitial_rad
        """
        self.setThetaInitial_rad(polarAngleInitial_rad)
        self.setPhiInitial_rad(azimuthalAngleInitial_rad)
        self.init()

    def init(self):
        """
        Initialisation for the computation of the cosine director.
        """
        self._init()

    def _init(self):
        pass

    def setThetaInitial_rad(self, polarAngleInitial_rad):
        """
        Set the initial polar angle.
        \param[in] polarAngleInitial_rad
        """
        self._thetaInitial_rad = polarAngleInitial_rad

    def getThetaInitial_rad(self):
        """
        Get the initial polar angle.
        """
        return self._thetaInitial_rad

    def setPhiInitial_rad(self, azimuthalAngleInitial_rad):
        """
        Set the initial azimuthal angle.
        param[in] azimuthalAngleInitial_rad
        """
        self._phiInitial_rad = azimuthalAngleInitial_rad

    def getPhiInitial_rad(self):
        """
        Get the initial azimuthal angle.
        """
        return self._phiInitial_rad

    def computeNewDirection(self, lastDirection, theta_rad, phi_rad):
        """
        Model from Joy book (1995) pages 31--32.
        """
        cx, cy, cz = lastDirection

        assert round(cx**2 + cy**2 + cz**2, 5) == round(1.0, 5)

        ca, cb, cc = self._computeNewDirection(cx, cy, cz, theta_rad, phi_rad)

        assert round(ca**2 + cb**2 + cc**2, 5) == round(1.0, 5)

        newDirection = (ca, cb, cc)
        return newDirection

class DirectionCosineJoy(DirectionCosine):
    def _computeNewDirection(self, cx, cy, cz, theta_rad, phi_rad):
        AN = -(cx/cz)
        AM = 1.0/math.sqrt(1.0 + AN*AN)

        V1 = AM * math.sin(theta_rad)
        V2 = AN * AM * math.sin(theta_rad)
        V3 = math.cos(phi_rad)
        V4 = math.sin(phi_rad)

        ca = cx*math.cos(theta_rad) + V1*V3 + cy*V2*V4
        cb = cy*math.cos(theta_rad) + V4 * (cz*V1 - cx*V2)
        cc = cz*math.cos(theta_rad) + V2*V3 - cy*V1*V4

        return ca, cb, cc

class DirectionCosineDemers(DirectionCosine):
    def _init(self):
        """
        Initialization of the Demers algorithm for the direction cosine calculation.
        The derivation of Demers (2000) is used.
        """
        self._previousMatrix = [[0.0, 0.0, 0.0],
                                [0.0, 0.0, 0.0],
                                [0.0, 0.0, 0.0]]

        self._currentMatrix = [[0.0, 0.0, 0.0],
                               [0.0, 0.0, 0.0],
                               [0.0, 0.0, 0.0]]

        a1 = math.cos(self._thetaInitial_rad)

        a2 = math.sin(self._thetaInitial_rad)

        a3 = math.cos(self._phiInitial_rad)

        a4 = math.sin(self._phiInitial_rad)

        for j in range(3):
            for k in range(3):
                self._previousMatrix[j][k] = 0.0
                self._currentMatrix[j][k] = 0.0

        self._previousMatrix[0][0] = 1.0
        self._previousMatrix[1][1] = 1.0
        self._previousMatrix[2][2] = 1.0

        self._currentMatrix[0][0] = (    (self._previousMatrix[0][0]*a3*a1) +
                                                      (self._previousMatrix[0][1]*a4*a1) -
                                    (self._previousMatrix[0][2]*a2))

        self._currentMatrix[0][1] = ((self._previousMatrix[0][1]*a3) - (self._previousMatrix[0][0]*a4))

        self._currentMatrix[0][2] = (    (self._previousMatrix[0][0]*a3*a2) +
                                                      (self._previousMatrix[0][1]*a4*a2) +
                                    (self._previousMatrix[0][2]*a1))

        self._currentMatrix[1][0] = (    (self._previousMatrix[1][0]*a3*a1) +
                                                      (self._previousMatrix[1][1]*a4*a1) -
                                    (self._previousMatrix[1][2]*a2))

        self._currentMatrix[1][1] = ((self._previousMatrix[1][1]*a3) - (self._previousMatrix[1][0]*a4))

        self._currentMatrix[1][2] = (    (self._previousMatrix[1][0]*a3*a2) +
                                                      (self._previousMatrix[1][1]*a4*a2) +
                                    (self._previousMatrix[1][2]*a1))

        self._currentMatrix[2][0] = (    (self._previousMatrix[2][0]*a3*a1) +
                                                      (self._previousMatrix[2][1]*a4*a1) -
                                    (self._previousMatrix[2][2]*a2))

        self._currentMatrix[2][1] = ((self._previousMatrix[2][1]*a3) - (self._previousMatrix[2][0]*a4))

        self._currentMatrix[2][2] = (    (self._previousMatrix[2][0]*a3*a2) +
                                                      (self._previousMatrix[2][1]*a4*a2) +
                                    (self._previousMatrix[2][2]*a1))

        for j in range(3):
            for k in range(3):
                self._previousMatrix[j][k] = self._currentMatrix[j][k]

    def _computeNewDirection(self, cx, cy, cz, theta_rad, phi_rad):
        """
        The function computes the direct cosines given a new set of
        collision angles. The derivation of Demers (2000) is used.
        [R] = 1
        [polarAngle] = rad
        [azimuthalAngle] = rad

        Demers algorithm for the direction cosine calculation.

        param[in] polarAngle_rad
        param[in] azimuthalAngle_rad
        """
        polarAngle_rad = theta_rad
        azimuthalAngle_rad = phi_rad

        a1 = math.cos(polarAngle_rad)

        a2 = math.sin(polarAngle_rad)

        a3 = math.cos(azimuthalAngle_rad)

        a4 = math.sin(azimuthalAngle_rad)

        self._currentMatrix[0][0] = ((self._previousMatrix[0][0]*a3*a1) + (self._previousMatrix[0][1]*a4*a1) -
                  (self._previousMatrix[0][2]*a2))

        self._currentMatrix[0][1] = ((self._previousMatrix[0][1]*a3)    - (self._previousMatrix[0][0]*a4))

        self._currentMatrix[0][2] = ((self._previousMatrix[0][0]*a3*a2) + (self._previousMatrix[0][1]*a4*a2) +
                  (self._previousMatrix[0][2]*a1))

        self._currentMatrix[1][0] = ((self._previousMatrix[1][0]*a3*a1) + (self._previousMatrix[1][1]*a4*a1) -
                  (self._previousMatrix[1][2]*a2))

        self._currentMatrix[1][1] = ((self._previousMatrix[1][1]*a3)    - (self._previousMatrix[1][0]*a4))

        self._currentMatrix[1][2] = ((self._previousMatrix[1][0]*a3*a2) + (self._previousMatrix[1][1]*a4*a2) +
                  (self._previousMatrix[1][2]*a1))

        self._currentMatrix[2][0] = ((self._previousMatrix[2][0]*a3*a1) + (self._previousMatrix[2][1]*a4*a1) -
                  (self._previousMatrix[2][2]*a2))

        self._currentMatrix[2][1] = ((self._previousMatrix[2][1]*a3)    - (self._previousMatrix[2][0]*a4))

        self._currentMatrix[2][2] = ((self._previousMatrix[2][0]*a3*a2) + (self._previousMatrix[2][1]*a4*a2) +
                  (self._previousMatrix[2][2]*a1))

        newDirection = (self._currentMatrix[0][2], self._currentMatrix[1][2], -1.0*self._currentMatrix[2][2])

        for j in range(3):
            for k in range(3):
                self._previousMatrix[j][k] = self._currentMatrix[j][k]

        return newDirection

class DirectionCosineDemersS(DirectionCosine):
    def _init(self):
        """
        Initialization of the Demers algorithm for the direction cosine calculation.
        """
        self._previousMatrix = [[0.0, 0.0, 0.0],
                                [0.0, 0.0, 0.0],
                                [0.0, 0.0, 0.0]]

        self._currentMatrix = [[0.0, 0.0, 0.0],
                               [0.0, 0.0, 0.0],
                               [0.0, 0.0, 0.0]]

        for j in range(3):
            for k in range(3):
                self._previousMatrix[j][k] = 0.0
                self._currentMatrix[j][k] = 0.0

        self._previousMatrix[0][0] = 1.0
        self._previousMatrix[1][1] = 1.0
        self._previousMatrix[2][2] = 1.0

        errno = 0
        a1 = math.cos(self._thetaInitial_rad)
        a2 = math.sin(self._thetaInitial_rad)
        a3 = math.cos(self._phiInitial_rad)
        a4 = math.sin(self._phiInitial_rad)

        self._currentMatrix[0][0] = (    (self._previousMatrix[0][0]*a3*a1) +
                                                      (self._previousMatrix[0][1]*a4*a1) -
                                    (self._previousMatrix[0][2]*a2))

        self._currentMatrix[0][1] = ((self._previousMatrix[0][1]*a3) - (self._previousMatrix[0][0]*a4))

        self._currentMatrix[0][2] = (    (self._previousMatrix[0][0]*a3*a2) +
                                                      (self._previousMatrix[0][1]*a4*a2) +
                                    (self._previousMatrix[0][2]*a1))

        self._currentMatrix[1][0] = (    (self._previousMatrix[1][0]*a3*a1) +
                                                      (self._previousMatrix[1][1]*a4*a1) -
                                    (self._previousMatrix[1][2]*a2))

        self._currentMatrix[1][1] = ((self._previousMatrix[1][1]*a3) - (self._previousMatrix[1][0]*a4))

        self._currentMatrix[1][2] = (    (self._previousMatrix[1][0]*a3*a2) +
                                                      (self._previousMatrix[1][1]*a4*a2) +
                                    (self._previousMatrix[1][2]*a1))

        self._currentMatrix[2][0] = (    (self._previousMatrix[2][0]*a3*a1) +
                                                      (self._previousMatrix[2][1]*a4*a1) -
                                    (self._previousMatrix[2][2]*a2))

        self._currentMatrix[2][1] = ((self._previousMatrix[2][1]*a3) - (self._previousMatrix[2][0]*a4))

        self._currentMatrix[2][2] = (    (self._previousMatrix[2][0]*a3*a2) +
                                                      (self._previousMatrix[2][1]*a4*a2) +
                                    (self._previousMatrix[2][2]*a1))

        for j in range(3):
            for k in range(3):
                self._previousMatrix[j][k] = self._currentMatrix[j][k]

        if(errno != 0):
            for j in range(3):
                for k in range(3):
                    self._previousMatrix[j][k] = 0.0
                    self._currentMatrix[j][k] = 0.0

        self._currentMatrix[0][0] = 1.0
        self._currentMatrix[1][1] = 1.0
        self._currentMatrix[2][2] = 1.0

        self._previousMatrix[0][0] = 1.0
        self._previousMatrix[1][1] = 1.0
        self._previousMatrix[2][2] = 1.0

    def _computeNewDirection(self, cx, cy, cz, theta_rad, phi_rad):
        """
        Demers algorithm for the direction cosine calculation.

        param[in] polarAngle_rad
        param[in] azimuthalAngle_rad
        """
        errno = 0
        polarAngle_rad = theta_rad
        azimuthalAngle_rad = phi_rad

        a1 = math.cos(polarAngle_rad)
        a2 = math.sin(polarAngle_rad)
        a3 = math.cos(azimuthalAngle_rad)
        a4 = math.sin(azimuthalAngle_rad)

        self._currentMatrix[0][0] = ((self._previousMatrix[0][0]*a3*a1) + (self._previousMatrix[0][1]*a4*a1) -
                  (self._previousMatrix[0][2]*a2))

        self._currentMatrix[0][1] = ((self._previousMatrix[0][1]*a3)    - (self._previousMatrix[0][0]*a4))

        self._currentMatrix[0][2] = ((self._previousMatrix[0][0]*a3*a2) + (self._previousMatrix[0][1]*a4*a2) +
                  (self._previousMatrix[0][2]*a1))

        self._currentMatrix[1][0] = ((self._previousMatrix[1][0]*a3*a1) + (self._previousMatrix[1][1]*a4*a1) -
                  (self._previousMatrix[1][2]*a2))

        self._currentMatrix[1][1] = ((self._previousMatrix[1][1]*a3)    - (self._previousMatrix[1][0]*a4))

        self._currentMatrix[1][2] = ((self._previousMatrix[1][0]*a3*a2) + (self._previousMatrix[1][1]*a4*a2) +
                  (self._previousMatrix[1][2]*a1))

        self._currentMatrix[2][0] = ((self._previousMatrix[2][0]*a3*a1) + (self._previousMatrix[2][1]*a4*a1) -
                  (self._previousMatrix[2][2]*a2))

        self._currentMatrix[2][1] = ((self._previousMatrix[2][1]*a3)    - (self._previousMatrix[2][0]*a4))

        self._currentMatrix[2][2] = ((self._previousMatrix[2][0]*a3*a2) + (self._previousMatrix[2][1]*a4*a2) +
                  (self._previousMatrix[2][2]*a1))

        newDirection = (self._currentMatrix[0][2], self._currentMatrix[1][2], -1.0*self._currentMatrix[2][2])

        for j in range(3):
            for k in range(3):
                self._previousMatrix[j][k] = self._currentMatrix[j][k]

        if errno != 0:
            for j in range(3):
                for k in range(3):
                    self._currentMatrix[j][k] = self._previousMatrix[j][k]

        newDirection = (self._currentMatrix[0][2], self._currentMatrix[1][2], -1.0*self._currentMatrix[2][2])
        return newDirection

class DirectionCosineSoum(DirectionCosine):
    def _init(self):
        """
        The function computes the direct cosines initial given a set of
        initial angles. The derivation of Soum et al. [1979] is used.
        [R] = 1
        [self._thetaInitial_rad] = rad
        [self._phiInitial_rad] = rad

        Initialization of the Soum algorithm for the direction cosine calculation.
        """

        a1 = math.cos(self._thetaInitial_rad)

        a2 = math.sin(self._thetaInitial_rad)

        a3 = math.cos(self._phiInitial_rad)

        a4 = math.sin(self._phiInitial_rad)

        self._previousDirection.setX(a2*a3)
        self._previousDirection.setY(a2*a4)
        self._previousDirection.setZ(-1.0*a1)

    def _computeNewDirection(self, cx, cy, cz, theta_rad, phi_rad):
        """
        The function computes the direct cosines given a new set of
        collision angles. The derivation of Soum et al. [1979] is used.
        [R] = 1
        [polarAngle] = rad
        [azimuthalAngle] = rad

        Soum algorithm for the direction cosine calculation.

        param[in] polarAngle_rad
        param[in] azimuthalAngle_rad
        """
        polarAngle_rad = theta_rad
        azimuthalAngle_rad = phi_rad

        a1 = math.cos(polarAngle_rad)

        a2 = math.sin(polarAngle_rad)

        a3 = math.cos(azimuthalAngle_rad)

        a4 = math.sin(azimuthalAngle_rad)

        a5 = a2*a3
        a6 = a2*a4

        rx0 = self._previousDirection.getX()
        ry0 = self._previousDirection.getY()
        rz0 = self._previousDirection.getZ()

        aa = rx0*rx0 + ry0*ry0

        if aa > 0.0:
            aa = math.sqrt(aa)

            if round(aa, 5) != 0.0:
                dx = ((-ry0*rx0*a5 + ry0*a6)/aa) + rx0*a1
                dy = (-(rz0*ry0*a5 + rx0*a6)/aa) + ry0*a1
                dz = aa*a5 + rz0*a1

                newDirection = (dx, dy, dz)
            else:
                newDirection = (a5, a6, a1)
        else:
            newDirection = (a5, a6, a1)

        self._previousDirection = newDirection

        return newDirection

class DirectionCosineDrouin(DirectionCosine):
    def _init(self):
        """
        The function computes the direct cosines initial given a set of
        initial angles. The derivation of Drouin & Gauvin (1997) is used.
        [R] = 1
        [self._thetaInitial_rad] = rad
        [self._phiInitial_rad] = rad

        Initialization of the Drouin algorithm for the direction cosine calculation.
        """
        a1 = math.cos(self._thetaInitial_rad)

        a2 = math.sin(self._thetaInitial_rad)

        a3 = math.cos(self._phiInitial_rad)

        a4 = math.sin(self._phiInitial_rad)

        self._previousDirection.setX(a2*a3)
        self._previousDirection.setY(a2*a4)
        self._previousDirection.setZ(-1.0*a1)

    def _computeNewDirection(self, cx, cy, cz, theta_rad, phi_rad):
        """
        The function computes the direct cosines given a new set of
        collision angles. The derivation of Drouin & Gauvin (1997) is used.
        [R] = 1
        [polarAngle] = rad
        [azimuthalAngle] = rad

        Drouin algorithm for the direction cosine calculation.

        param[in] polarAngle_rad
        param[in] azimuthalAngle_rad
        """
        polarAngle_rad = theta_rad
        azimuthalAngle_rad = phi_rad

        a1 = math.cos(polarAngle_rad)

        a2 = math.sin(polarAngle_rad)

        a3 = math.cos(azimuthalAngle_rad)

        a4 = math.sin(azimuthalAngle_rad)

        a5 = a2*a3
        a6 = a2*a4

        rx0 = self._previousDirection.getX()
        ry0 = self._previousDirection.getY()
        rz0 = self._previousDirection.getZ()

        aa = rx0*rx0+rz0*rz0
        ab = rx0*rx0*ry0*ry0+(rx0*rx0+rz0*rz0)*(rx0*rx0+rz0*rz0)+ry0*ry0*rz0*rz0

        if ab > 0.0:
            ab = math.sqrt(ab)
        else:
            ab = 1.0

        if aa > 0.0:
            aa = math.sqrt(aa)

            if rz0 > 0.0:
                if round(aa, 5) != 0.0:
                    dx = rz0*a5/aa+rx0*ry0*a6/ab+rx0*a1
                    dy = -a6*aa*aa/ab+ry0*a1
                    dz = -a5*rx0/aa+a6*rz0*ry0/ab+rz0*a1

                    newDirection = (dx, dy, dz)
                else:
                    newDirection = (a5, a6, a1)
            else:
                if round(aa, 5) != 0.0:
                    dx = -rz0*a5/aa-rx0*ry0*a6/ab+rx0*a1
                    dy = +a6*aa*aa/ab+ry0*a1
                    dz = +a5*rx0/aa-a6*rz0*ry0/ab+rz0*a1

                    newDirection = (dx, dy, dz)
                else:
                    newDirection = (a5, a6, a1)
        else:
            newDirection = (a5, a6, a1)

        self._previousDirection = newDirection

        return newDirection
