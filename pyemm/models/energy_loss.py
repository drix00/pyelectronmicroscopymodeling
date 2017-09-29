#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2009 Hendrix Demers"
__license__ = ""

# Standard library modules.
import os.path

# Third party modules.
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as constants

# Local modules.
import pywinxraydata.ElementProperties as ElementProperties
# import DatabasesTools.Casino3.SecondaryElectronData as SecondaryElectronData
import pyHendrixDemersTools.Files as Files
from pyHendrixDemersTools import Graphics

# Globals and constants variables.

class Region(object):
    def __init__(self):
        self._rho_g_cm3 = 0.0
        self._elements = []

class Element(object):
    def __init__(self):
        self._J = 0.0
        self._k = 0.0
        self._Z_A = 0.0
        self._rho = 0.0

def dEdsJoyLuoGauvin_eV_nm(atomicNumber, energy_eV):
    J_eV = ElementProperties.getMeanIonizationEnergy_eV(atomicNumber)
    k = ElementProperties.getKRatioCorrection(atomicNumber)
    Z_A = atomicNumber/ElementProperties.getAtomicMass_g_mol(atomicNumber)

    rho_g_cm3 = ElementProperties.getMassDensity_g_cm3(atomicNumber)

    B = np.log(1.166 * (energy_eV + k*J_eV)/J_eV) * Z_A

    dEds_eV_nm = -7.85 * rho_g_cm3 * B / (energy_eV*1.0e-3)

    return dEds_eV_nm

def dEdsBethe_eV_nm(atomicNumber, energy_eV):
    J_eV = ElementProperties.getMeanIonizationEnergy_eV(atomicNumber)
    Z_A = atomicNumber/ElementProperties.getAtomicMass_g_mol(atomicNumber)

    rho_g_cm3 = ElementProperties.getMassDensity_g_cm3(atomicNumber)

    B = np.log(1.166 * energy_eV/J_eV) * Z_A

    dEds_eV_nm = -7.85 * rho_g_cm3 * B / (energy_eV*1.0e-3)

    return dEds_eV_nm

def dEdsBetheRelativiste_eV_nm(atomicNumber, energy_eV):
    E0_eV = 511.0e3
    temp = (1.0 / (1.0 + energy_eV * (1.0 / E0_eV)))
    beta2 = _computeBeta2(energy_eV)
    sumConstant = np.log(temp*temp) + beta2

    J_eV = ElementProperties.getMeanIonizationEnergy_eV(atomicNumber)
    Z_A = atomicNumber/ElementProperties.getAtomicMass_g_mol(atomicNumber)

    B = (np.log(297.91*beta2 / (J_eV*1.0e-3)) - sumConstant)* Z_A

    rho_g_cm3 = ElementProperties.getMassDensity_g_cm3(atomicNumber)

    dEds_eV_nm = (-7.85 * 2.0 / (E0_eV*1.0e-3)) * rho_g_cm3 * B / (beta2)

    return dEds_eV_nm

def dEdsJoyLuoMonsel_eV_nm(atomicNumber, energy_eV):
    configurationFilepath = Files.getCurrentModulePath(__file__, "../EnergyLossTools.cfg")
    filepath = Files.getDataPath(configurationFilepath, os.path.join("Casino3", "int", "numlist.dat"))
    seData = SecondaryElectronData.SecondaryElectronData(filepath)

    J_eV = ElementProperties.getMeanIonizationEnergy_eV(atomicNumber)
    workFunction_eV = seData.getWorkFunction_eV(atomicNumber)
    k = ElementProperties.getKRatioCorrectionMonsel(atomicNumber, workFunction_eV*1.0e-3)
    Z_A = atomicNumber/ElementProperties.getAtomicMass_g_mol(atomicNumber)

    rho_g_cm3 = ElementProperties.getMassDensity_g_cm3(atomicNumber)

    B = np.log(1.166 * (energy_eV + k*J_eV)/J_eV) * Z_A

    dEds_eV_nm = -7.85 * rho_g_cm3 * B / (energy_eV*1.0e-3)

    if energy_eV*1.0e-3 < (workFunction_eV*1.0e-3 + 1.0 - 10.0):
        dEds_eV_nm = 0.0

    if dEds_eV_nm > 0.0:
        dEds_eV_nm = 0.0

    residualEnergyLoss_eV = 0.0004e-3
    return dEds_eV_nm - residualEnergyLoss_eV

def reimer2008BetheRelativistic_eV_nm(atomicNumber, energy_eV):
    """
    From Reimer TEM book's.

    Reimer (2008) page 188 equation (5.100)

    .. math:

         \left|\frac{\mathrm{d}E_{m}}{\mathrm{d}x}\right|_{B} = \frac{e^{4}N_{A}Z}{4\pi\epsilon_{0}^{2}A E_{0}\beta^{2}} \ln\left(\frac{E_{0}\beta^{2}}{2J}\right)

    :param atomicNumber:
    :param energy_eV:
    :return: energy loss in eV/nm.
    """
    J = ElementProperties.getMeanIonizationEnergy_eV(atomicNumber)
    Z = atomicNumber
    A = ElementProperties.getAtomicMass_g_mol(atomicNumber)
    rho_g_cm3 = ElementProperties.getMassDensity_g_cm3(atomicNumber)
    E_0 = constants.value("electron mass energy equivalent in MeV")*1.0E6
    e = constants.e
    N_A = constants.N_A
    pi = constants.pi
    #eps_0 = constants.epsilon_0
    #1.4185972E10-39 C2 eV-1 nm-1
    eps_0 = 1.4185972e-39
    beta2 = _computeBeta2(energy_eV)
    factorConstant = (e**4)*N_A/(4.0*pi*(eps_0**2)*E_0)
    factorElement = Z/(A*beta2)
    factorLog = E_0*beta2/(2.0*J)

    cm3_to_nm3 = 1.0e21
    dEds_eV_nm = -rho_g_cm3*factorConstant*factorElement*np.log(factorLog)/cm3_to_nm3
    return dEds_eV_nm

def reimer2008Bethe_eV_nm(atomicNumber, energy_eV):
    """
    From Reimer TEM book's.

    Reimer (2008) page 462 equation (11.2)

    .. math:

         \left|\frac{\mathrm{d}E_{m}}{\mathrm{d}x}\right|_{B} = 7.8\time 10^{4} \frac{Z}{A} \frac{1}{E} \ln\frac{E}{J}

    where :math:`E` in eV and :math:`\frac{\mathrm{d}E_{m}}{\mathrm{d}x}` in :math:`eV \mu g^{-1} cm^{2}`.

    :param atomicNumber:
    :param energy_eV:
    :return: energy loss in eV/nm.
    """
    J = ElementProperties.getMeanIonizationEnergy_eV(atomicNumber)
    Z = atomicNumber
    A = ElementProperties.getAtomicMass_g_mol(atomicNumber)
    rho_g_cm3 = ElementProperties.getMassDensity_g_cm3(atomicNumber)

    factorConstant = 7.8e4
    factorElement = Z/(A*energy_eV)
    factorLog = energy_eV/J

    cm2_ug_to_nm2_g = 1.0e1
    dEds_eV_nm = -rho_g_cm3*factorConstant*factorElement*np.log(factorLog)/cm2_ug_to_nm2_g
    return dEds_eV_nm

def _computeBeta2(energy_eV):
    E0_eV = 511.0e3
    temp = (1.0 / (1.0 + energy_eV / E0_eV))
    beta2 = 1.0 - temp * temp

    return beta2

def dEdsTurner1978(atomicNumber, energy_eV):
    """
    From CRC Handbook of Radiation Measurement and Protection
    in section 3.4 Stopping Powers and Ranges of Charged Particles by James E. Turner (pages 213--228).

    .. math:
        \left(-\frac{dE}{dx}\right)_{col} = \frac{2\pi e^{4} N Z}{mv^{2}} \left[ \ln \frac{T mv^{2}}{2 I^{2} \left(1 - \beta^{2}\right)} + 1 - \beta^{2} + \frac{1}{8} \left(1 - \sqrt{1 - \beta^{2}}\right) - \left( 2 \sqrt{1 - \beta^{2}} - 1 + \beta^{2}\right)\ln 2 - \delta \right]

    """
    return 0.0

def run():
    Graphics.setDefaultDisplay()

    atomicNumber = 29
    energies_eV = np.arange(5.0e3, 500.0e3, 5.0e3)
    dEdsModels = {"Joy Luo Gauvin": dEdsJoyLuoGauvin_eV_nm,
                                "Joy Luo Monsel": dEdsJoyLuoMonsel_eV_nm,
                                "Bethe": dEdsBethe_eV_nm,
                                "Bethe Relativiste": dEdsBetheRelativiste_eV_nm,
                                "Reimer 2008 Bethe Relativiste": reimer2008BetheRelativistic_eV_nm,
                                "Reimer 2008 Bethe": reimer2008Bethe_eV_nm}

    plt.figure()
    plt.title(atomicNumber)

    for label in dEdsModels:
        y = [dEdsModels[label](atomicNumber, energy_eV) for energy_eV in energies_eV]
        if label == "Reimer 2008 Bethe":
            plt.plot(energies_eV, y, '.', label=label)
        else:
            plt.plot(energies_eV, y, label=label)

    plt.xlabel("Energy (eV)")
    plt.ylabel("dE/ds (eV/nm)")
    plt.legend(loc='best')

    energies_eV = np.arange(1.0e3, 5.0e3, 5.0)
    dEdsModels = {"Joy Luo Gauvin": dEdsJoyLuoGauvin_eV_nm,
                                "Joy Luo Monsel": dEdsJoyLuoMonsel_eV_nm,
                                "Bethe": dEdsBethe_eV_nm,
                                "Bethe Relativiste": dEdsBetheRelativiste_eV_nm,
                                "Reimer 2008 Bethe Relativiste": reimer2008BetheRelativistic_eV_nm,
                                "Reimer 2008 Bethe": reimer2008Bethe_eV_nm}

    plt.figure()
    plt.title("Low energy: %i" % (atomicNumber))

    for label in dEdsModels:
        y = [dEdsModels[label](atomicNumber, energy_eV) for energy_eV in energies_eV]
        if label == "Reimer 2008 Bethe":
            plt.plot(energies_eV, y, '.', label=label)
        else:
            plt.plot(energies_eV, y, label=label)

    plt.xlabel("Energy (eV)")
    plt.ylabel("dE/ds (eV/nm)")
    plt.legend(loc='best')

    energies_eV = np.arange(1.0, 500.0, 1.0)
    dEdsModels = {"Joy Luo Gauvin": dEdsJoyLuoGauvin_eV_nm,
                                "Joy Luo Monsel": dEdsJoyLuoMonsel_eV_nm}

    plt.figure()
    plt.title("Very low energy: %i" % (atomicNumber))

    for label in dEdsModels:
        y = [dEdsModels[label](atomicNumber, energy_eV) for energy_eV in energies_eV]
        plt.plot(energies_eV, y, label=label)

    plt.xlabel("Energy (eV)")
    plt.ylabel("dE/ds (eV/nm)")
    plt.legend(loc='best')

    plt.show()

def runCasino():
    Graphics.setDefaultDisplay()

    atomicNumber = 29
    energies_eV = np.arange(5.0e3, 500.0e3, 5.0e3)
    dEdsModels = {"Joy Luo Gauvin": dEdsJoyLuoGauvin_eV_nm,
                  "Joy Luo Monsel": dEdsJoyLuoMonsel_eV_nm}

    plt.figure()
    plt.title(atomicNumber)

    for label in dEdsModels:
        y = [dEdsModels[label](atomicNumber, energy_eV) for energy_eV in energies_eV]
        if label == "Reimer 2008 Bethe":
            plt.plot(energies_eV, y, 'o', label=label)
        else:
            plt.plot(energies_eV, y, label=label)

    plt.xlabel("Energy (eV)")
    plt.ylabel("dE/ds (eV/nm)")
    plt.legend(loc='best')

    energies_eV = np.arange(1.0e3, 5.0e3, 5.0)
    dEdsModels = {"Joy Luo Gauvin": dEdsJoyLuoGauvin_eV_nm,
                  "Joy Luo Monsel": dEdsJoyLuoMonsel_eV_nm}

    plt.figure()
    plt.title("Low energy: %i" % (atomicNumber))

    for label in dEdsModels:
        y = [dEdsModels[label](atomicNumber, energy_eV) for energy_eV in energies_eV]
        if label == "Reimer 2008 Bethe":
            plt.plot(energies_eV, y, 'o', label=label)
        else:
            plt.plot(energies_eV, y, label=label)

    plt.xlabel("Energy (eV)")
    plt.ylabel("dE/ds (eV/nm)")
    plt.legend(loc='best')

    energies_eV = np.arange(1.0, 500.0, 1.0)
    dEdsModels = {"Joy Luo Gauvin": dEdsJoyLuoGauvin_eV_nm,
                  "Joy Luo Monsel": dEdsJoyLuoMonsel_eV_nm}

    plt.figure()
    plt.title("Very low energy: %i" % (atomicNumber))

    for label in dEdsModels:
        y = [dEdsModels[label](atomicNumber, energy_eV) for energy_eV in energies_eV]
        plt.plot(energies_eV, y, label=label)

    plt.xlabel("Energy (eV)")
    plt.ylabel("dE/ds (eV/nm)")
    plt.legend(loc='best')

    plt.show()

def runCRDGauvinBruker():
    Graphics.setDefaultDisplay()

    atomicNumber = 29
    energies_eV = np.arange(60.0e3, 400.0e3, 1.0e3)
#    dEdsModels = {"Joy Luo Gauvin": dEdsJoyLuoGauvin_eV_nm,
#                  "Joy Luo Monsel": dEdsJoyLuoMonsel_eV_nm,
#                  "Bethe": dEdsBethe_eV_nm,
#                  "Bethe Relativiste": dEdsBetheRelativiste_eV_nm,
#                  "Reimer 2008 Bethe Relativiste": reimer2008BetheRelativistic_eV_nm,
#                  "Reimer 2008 Bethe": reimer2008Bethe_eV_nm}

#    dEdsModels = {"Joy Luo Gauvin": dEdsJoyLuoGauvin_eV_nm,
#                  "Joy Luo Monsel": dEdsJoyLuoMonsel_eV_nm}

#    dEdsModels = {"Bethe": dEdsBethe_eV_nm,
#                  "Reimer 2008 Bethe": reimer2008Bethe_eV_nm}

#    dEdsModels = {"Bethe Relativiste": dEdsBetheRelativiste_eV_nm,
#                  "Reimer 2008 Bethe Relativiste": reimer2008BetheRelativistic_eV_nm}

    dEdsModels = {"Joy Luo Gauvin": dEdsJoyLuoGauvin_eV_nm,
                  "Bethe": dEdsBethe_eV_nm,
                  "Bethe Relativiste": dEdsBetheRelativiste_eV_nm,
                  "Reimer 2008 Bethe Relativiste": reimer2008BetheRelativistic_eV_nm}

    plt.figure()
    plt.title(atomicNumber)

    for label in dEdsModels:
        y = [dEdsModels[label](atomicNumber, energy_eV) for energy_eV in energies_eV]
        if label == "Joy Luo Gauvin":
            plt.plot(energies_eV, y, 'o', label=label)
        else:
            plt.plot(energies_eV, y, label=label)

    plt.xlabel("Energy (eV)")
    plt.ylabel("dE/ds (eV/nm)")
    plt.legend(loc='best')

    plt.show()

if __name__ == '__main__':    #pragma: no cover
    run()
