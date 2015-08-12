#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2011 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision$"
__svnDate__ = "$Date$"
__svnId__ = "$Id$"

# Standard library modules.
import pprint
import time

# Third party modules.

# Local modules.

# Project modules
import pyemm.montecarlo.engine as MonteCarloEngine

# Globals and constants variables.

def run(): #pragma: no cover
    numberElectrons = 200
    atomicNumbers = [6, 79]
    energies_keV = [1.0, 10.0]
    energies_eV = [energy_keV*1.0e3 for energy_keV in energies_keV]

    bseResults = {}

    for atomicNumber in atomicNumbers:
        bseResults.setdefault(atomicNumber, {})
        for energy_eV in energies_eV:
            engine = MonteCarloEngine.createEngine()

            engine.setSampleBulk(atomicNumber=atomicNumber)
            engine.setBeamEnergy_eV(energy_eV)

            engine.simulate(numberElectrons=numberElectrons)

            bse = engine.getBackscatteredElectronCoefficient()
            bseResults[atomicNumber][energy_eV] = bse

    pprint.pprint(bseResults)
    time.sleep(0.5)

if __name__ == '__main__':  #pragma: no cover
    run()
