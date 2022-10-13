# -*- coding: utf-8 -*-
"""
@Author: Iris Agresti, Mathias Pont and Andreas Fyrillas
"""

import itertools as it

import matplotlib.pyplot as plt
import numpy as np

import QuantumTomography as qLib


output_states = np.array(['0000', '0001', '0010', '0011', 
                          '0100', '0101', '0110', '0111', 
                          '1000', '1001', '1010', '1011',
                          '1100', '1101', '1110', '1111'])

def density_matrix_4GHZ(angle=np.pi/4):
    """
    :return: the density matrix of a 4 GHZ state
    """
    state = (2 ** 4) * [0]
    state[5] = 1
    state[10] = np.tan(angle)
    state = state/np.sqrt(2)

    rho_th = np.kron(state, state).reshape(len(state), len(state))
    return rho_th

def get_msr():
    """
    :return: array with the measurements of the density matrix
    """
    meas = list(it.product(['X', 'Y', 'Z'], repeat=4))
    msr = []
    # list of eigenvectors of X,Y,Z
    se = [[1 / np.sqrt(2), 1 / np.sqrt(2)], \
          [1 / np.sqrt(2), 1j / np.sqrt(2)], \
          [1, 0]]
    for m in meas:
        ind = []
        for x in range(4):
            if m[x] == 'X':
                ind.append(0)
            if m[x] == 'Y':
                ind.append(1)
            if m[x] == 'Z':
                ind.append(2)
        msr.append([se[ind[0]][0], se[ind[0]][1], se[ind[1]][0], se[ind[1]][1], \
                    se[ind[2]][0], se[ind[2]][1], se[ind[3]][0], se[ind[3]][1]])

    return np.array(msr)


def get_tomography(counts):
    """
    :param counts: array with the 81 histograms
    :return: density matrix
    """
    measurements = get_msr()

    tot_counts = []
    for histo in counts:
        tot_counts.append(np.sum(histo))

    tomo_obj = qLib.Tomography()

    tomo_in = tomo_obj.buildTomoInput(measurements=measurements,
                                      counts=counts,
                                      crosstalk=-1,
                                      efficiency=-1,
                                      time=-1,
                                      singles=-1,
                                      window=0,
                                      error=0)

    [rhog, boh, fval] = tomo_obj.StateTomography_Matrix(tomo_in, method='MLE')

    rho_expected = density_matrix_4GHZ()
    f = qLib.fidelity(rhog, rho_expected)
    p = qLib.purity(rhog)

    print('Fidelity = ' + str(f))
    print('Purity = ' + str(p))

    return rhog, boh, fval