#!/usr/bin/env python
"""
.. py:currentmodule:: electronmagnetic.uniform_magnetic_field
   :synopsis: Uniform mangetic fields.

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Uniform mangetic fields.
"""

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = "0.1"
__date__ = "Oct 9, 2015"
__copyright__ = "Copyright (c) 2015 Hendrix Demers"
__license__ = "GPL 3"

# Standard library modules.

# Third party modules.
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from scipy.constants import e, m_e, c

# Local modules.

# Project modules

# Globals and constants variables.
ELECTRON_REST_MASS_kg = m_e
ELECTRON_REST_ENERGY_keV = 511.0
LIGHT_VELOCITY_m_s = c

X = 0
Y = 1
Z = 2

def compute_velocity_nm_s(electron_energy_keV):
    """
    .. todo:: Correct the implementation of this method with reference.
    :param electron_energy_keV:
    :return:
    """
    energy_eV = electron_energy_keV * 1.0e3
    energy_Nm = energy_eV * 1.602189e-19
    velocity_m_s = np.sqrt(2.0*energy_Nm/m_e)
    velocity_nm_s = velocity_m_s*1.0e9

    return velocity_nm_s

def compute_relativistic_velocity_nm_s(electron_energy_keV):
    relativistic_factor = 1.0 + electron_energy_keV / ELECTRON_REST_ENERGY_keV

    velocity_m_s = LIGHT_VELOCITY_m_s * np.sqrt(1.0 -  1.0/(relativistic_factor * relativistic_factor))
    velocity_nm_s = velocity_m_s*1.0e9

    return velocity_nm_s

def compute_acceleration_m_s2(velocity_magnitude_m_s, direction, magnetic_field_T):
    acceleration_m_s2 = np.zeros(3)
    factor_Cm_skg = -e * velocity_magnitude_m_s / m_e

    acceleration_m_s2[X] = direction[Y] * magnetic_field_T[Z] - direction[Z] * magnetic_field_T[Y]
    acceleration_m_s2[Y] = direction[Z] * magnetic_field_T[X] - direction[X] * magnetic_field_T[Z]
    acceleration_m_s2[Z] = direction[X] * magnetic_field_T[Y] - direction[Y] * magnetic_field_T[X]

    acceleration_m_s2 *= factor_Cm_skg
    return acceleration_m_s2

def compute_time_s(step_length_nm, velocity_magnitude_m_s):
    step_length_m = step_length_nm * 1.0e-9
    time_s = step_length_m / velocity_magnitude_m_s
    return time_s

def compute_new_positions_nm(old_positions_nm, velocity_m_s, acceleration_m_s2, time_s):
    delta_positions_m = velocity_m_s * time_s + (1.0/2.0) * acceleration_m_s2 *time_s * time_s
    delta_positions_nm = delta_positions_m * 1.0e9
    new_positions_nm = old_positions_nm + delta_positions_nm
    return new_positions_nm

def update_trajectory(number, positions_nm, line):
    line.set_data(positions_nm[0:2, :number])
    line.set_3d_properties(positions_nm[2, :number])
    return line

def simulation(initial_direction, number_steps, electron_energy_keV, magnetic_field_T, step_length_nm):
    direction = initial_direction
    positions_nm = np.zeros((3, number_steps))
    for step_ID in range(1, number_steps, 1):
        velocity_magnitude_nm_s = compute_relativistic_velocity_nm_s(electron_energy_keV)
        velocity_magnitude_m_s = velocity_magnitude_nm_s * 1.0e-9

        acceleration_m_s2 = compute_acceleration_m_s2(velocity_magnitude_m_s, direction, magnetic_field_T)

        time_s = compute_time_s(step_length_nm, velocity_magnitude_m_s)

        velocity_m_s = direction*velocity_magnitude_m_s
        new_positions_nm = compute_new_positions_nm(positions_nm[:, step_ID-1], velocity_m_s, acceleration_m_s2, time_s)
        positions_nm[:, step_ID] = new_positions_nm

        delta_positions_nm = positions_nm[:, step_ID] - positions_nm[:, step_ID-1]
        direction = (delta_positions_nm) / np.linalg.norm(delta_positions_nm)

        #message = "%4i (%.3g, %.3g, %.3g)" % (step_ID, positions_nm[0, step_ID], positions_nm[1, step_ID], positions_nm[2, step_ID])
        #print(message)

    return positions_nm

def run():
    electron_energy_keV = 1.0
    magnetic_field_T = np.array((0.0, 0.0, 1.0))
    initial_direction = np.array((1.0, 0.0, 1.0))
    initial_direction /= np.linalg.norm(initial_direction)
    step_length_nm = 100.0
    number_steps = 200000

    positions_nm = simulation(initial_direction, number_steps, electron_energy_keV, magnetic_field_T, step_length_nm)

    plot(positions_nm)
    #plot_animation(positions_nm, number_steps)

def run_penelope2008():
    electron_energy_keV = 0.5e3
    magnetic_field_T = np.array((0.0, 0.0, 0.2))
    initial_direction = np.array((1.0, 0.0, 1.0))
    initial_direction /= np.linalg.norm(initial_direction)
    step_length_nm = 1.0e5
    number_steps = 20000

    positions_nm = simulation(initial_direction, number_steps, electron_energy_keV, magnetic_field_T, step_length_nm)

    plotXZ(positions_nm)

def plot(positions_nm):
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    ax.plot(positions_nm[0, :], positions_nm[1, :], positions_nm[2, :], '.')

    limit = np.max(positions_nm[X])
    ax.set_xlim3d([-1.0*limit, 1.0*limit])
    ax.set_xlabel('X (nm)')

    limit = np.max(positions_nm[Y])
    ax.set_ylim3d([-1.0*limit, 1.0*limit])
    ax.set_ylabel('Y (nm)')

    limit = np.max(positions_nm[Z])
    ax.set_zlim3d([-1.0*limit, 1.0*limit])
    ax.set_zlabel('Z (nm)')

    ax.set_title('Uniform magnetic field')

def plot_animation(positions_nm, number_steps):
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    line = ax.plot(positions_nm[0, 0:1], positions_nm[1, 0:1], positions_nm[2, 0:1])[0]


    limit = np.max(positions_nm)
    ax.set_xlim3d([-1.0*limit, 1.0*limit])
    ax.set_xlabel('X (nm)')

    ax.set_ylim3d([-1.0*limit, 1.0*limit])
    ax.set_ylabel('Y (nm)')

    ax.set_zlim3d([-1.0*limit, 1.0*limit])
    ax.set_zlabel('Z (nm)')

    ax.set_title('Uniform magnetic field')

    # Creating the Animation object
    number = int(number_steps/1000.0)
    line_ani = animation.FuncAnimation(fig, update_trajectory, number, fargs=(positions_nm, line),
                                  interval=50, blit=False)

def plotXZ(positions_nm):
    positions_cm = positions_nm*1.0e-7
    plt.figure()

    plt.plot(positions_cm[Z], positions_cm[X])

    plt.xlim((0.0, 40.0))
    plt.ylim((-5, 5))

if __name__ == '__main__':
    #run()
    run_penelope2008()

    plt.show()
