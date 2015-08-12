#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2009 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision$"
__svnDate__ = "$Date$"
__svnId__ = "$Id$"

# Standard library modules.
import csv

# Third party modules.
import matplotlib.pyplot as plt

# Local modules.
import DrixUtilities.Files as Files
import numpy as np

import EnergyLoss

# Globals and constants variables.
ENERGIES_eV = "energies_eV"
STOPPING_POWER_COLLISION_eV_nm = "stoppingPowerCollisions_eV_nm"
STOPPING_POWER_TOTAL_eV_nm = "stoppingPowerTotals_eV_nm"

EXPERIMENTAL = "Experimental"

class AnalyzeWater(object):
    def __init__(self):
        self._rhoWater_g_cm3 = 1.0

        self._results = {}
        self._readExperimentalData()

    def _readExperimentalData(self):
        configurationFilepath = Files.getCurrentModulePath(__file__, "EnergyLossTools.cfg")
        dataFilepath = Files.getDataPath(configurationFilepath, "CRCHandbook1978/Table_3.4.5_MassStoppingPowersElectron_water.csv")

        reader = csv.reader(open(dataFilepath, 'rb'))

        dummy_headerRow = reader.next()

        energies_eV = []
        stoppingPowerCollisions_eV_nm = []
        stoppingPowerTotals_eV_nm = []

        for row in reader:
            try:
                energy_MeV = float(row[0])
                SCollision_MeVcm2_g = float(row[1])
                STotal_MeVcm2_g = float(row[2])

                energies_eV.append(energy_MeV*1.0e6)
                stoppingPowerCollisions_eV_nm.append(SCollision_MeVcm2_g*1.0e6/self._rhoWater_g_cm3/1.0e7)
                stoppingPowerTotals_eV_nm.append(STotal_MeVcm2_g*1.0e6/self._rhoWater_g_cm3/1.0e7)
            except ValueError:
                pass

        results = {}
        results[ENERGIES_eV] = energies_eV
        results[STOPPING_POWER_COLLISION_eV_nm] = stoppingPowerCollisions_eV_nm
        results[STOPPING_POWER_TOTAL_eV_nm] = stoppingPowerTotals_eV_nm

        self._results[EXPERIMENTAL] = results

    def doGraphics(self):
        plt.figure()

        x = np.array(self._results[EXPERIMENTAL][ENERGIES_eV])
        yCollision = np.array(self._results[EXPERIMENTAL][STOPPING_POWER_COLLISION_eV_nm])
        yTotal = np.array(self._results[EXPERIMENTAL][STOPPING_POWER_TOTAL_eV_nm])
        yBrem = yTotal - yCollision

        meanZ = 7
        #yBethe_eV_nm = -EnergyLoss.dEdsBethe_eV_nm(meanZ, x)
        yBetheRelativiste_eV_nm = -EnergyLoss.dEdsBetheRelativiste_eV_nm(meanZ, x)
        #yJoyLuoGauvin_eV_nm = -EnergyLoss.dEdsJoyLuoGauvin_eV_nm(meanZ, x)
        yBetheRelativiste2_eV_nm = (-2.0*EnergyLoss.dEdsBetheRelativiste_eV_nm(1, x) - EnergyLoss.dEdsBetheRelativiste_eV_nm(8, x))
        yBetheRelativiste3_eV_nm = -0.111895*EnergyLoss.dEdsBetheRelativiste_eV_nm(1, x) - 0.888105*EnergyLoss.dEdsBetheRelativiste_eV_nm(8, x)

        plt.semilogx(x, yCollision, label="Collision")
        plt.semilogx(x, yBrem, label="Bremsstrahlung")
        plt.semilogx(x, yTotal, label="Total")

        #plt.semilogx(x, yBethe_eV_nm, 'o', label="Bethe")
        plt.semilogx(x, yBetheRelativiste_eV_nm, '.', label="Bethe Relativiste")
        #plt.semilogx(x, yJoyLuoGauvin_eV_nm, 'x', label="JoyLuoGauvin")
        plt.semilogx(x, yBetheRelativiste2_eV_nm, '.', label="Bethe Relativiste atomic fraction")
        plt.semilogx(x, yBetheRelativiste3_eV_nm, '.', label="Bethe Relativiste weight fraction")

        plt.xlabel("Energy (eV)")
        plt.ylabel("Stopping power (eV/nm)")
        plt.legend(loc='best')
        #plt.xlim(xmax=500.0e3)
        plt.show()

def run():
    analyze = AnalyzeWater()

    analyze.doGraphics()

if __name__ == '__main__':    #pragma: no cover
    import DrixUtilities.Runner as Runner
    Runner.Runner().run(runFunction=run)
