import itertools
import os
import numpy as np
import glob
import operator
import time
from datetime import datetime

def set_filename(folder, name="Dataset", extension="", in_folder=""):
    # This module creates a folder with the date of today and a file named "string" with extension "extension"
    now = datetime.now()
    dt_string = now.strftime("%b-%d-%Y")

    if in_folder == "":
        newpath = folder + os.sep + dt_string
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    else:
        newpath = folder + os.sep + dt_string + os.sep + in_folder
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    i = 0
    while os.path.exists(newpath + os.sep + name + "%s" % i + extension):
        i += 1

    filename = newpath + os.sep + name + "%s" % i + extension

    return filename

# Utils
def get_sorted_filenames(mypath):
    '''

    :param mypath: path with / at the end
    :return: reordered_filenames_before {indice in density matrix: [base of measurement, filename]}
    '''

    os.chdir(mypath)
    files = glob.glob('*.npy')

    filenames_before = {}
    filenames_after = {}
    filenames_current = {}
    for file in [x for x in files if 'before' in x]:
        emp_str = ""
        for m in file:
            if m.isdigit():
                emp_str = emp_str + m
                n = int(emp_str) / 10
        filenames_before[n] = file

    for file in [x for x in files if 'after' in x]:
        emp_str = ""
        for m in file:
            if m.isdigit():
                emp_str = emp_str + m
                n = int(emp_str) / 10
        filenames_after[n] = file

    for file in [x for x in files if 'current' in x]:
        emp_str = ""
        for m in file:
            if m.isdigit():
                emp_str = emp_str + m
                n = int(emp_str) / 10
        filenames_current[n] = file

    reordered_filenames_before = dict(sorted(filenames_before.items(), key=operator.itemgetter(0)))
    reordered_filenames_after = dict(sorted(filenames_after.items(), key=operator.itemgetter(0)))
    reordered_filenames_current = dict(sorted(filenames_current.items(), key=operator.itemgetter(0)))

    return reordered_filenames_before, reordered_filenames_after, reordered_filenames_current


def gate_fidelity(path):
    density_matrix = list(itertools.product(['sigmax', 'sigmay', 'sigmaz'], repeat=4))

    reordered_filenames_before, reordered_filenames_after, _ = get_sorted_filenames(path)

    party_before_dict = {}
    party_after_dict = {}

    for idx, filename in enumerate(reordered_filenames_before):
        before_arr = np.load(file=path + reordered_filenames_before[filename])[0]
        after_arr = np.load(file=path + reordered_filenames_after[filename])[0]

        all_phases_before = []
        all_phases_after = []
        for party, measurement in enumerate(density_matrix[idx]):
            if measurement == 'sigmay':
                all_phases_before.append(np.array([np.pi / 2, before_arr[party]]))
                all_phases_after.append(np.array([np.pi / 2, after_arr[party]]))
            else:
                all_phases_before.append(np.array([0, before_arr[party]]))
                all_phases_after.append(np.array([0, after_arr[party]]))

        party_before_dict[density_matrix[idx]] = np.array(all_phases_before)
        party_after_dict[density_matrix[idx]] = np.array(all_phases_after)

    return party_before_dict, party_after_dict


def set_filename(folder, name="Dataset", extension="txt", in_folder=""):
    # This module creates a folder with the date of today and a file named "string" with extension "extension"
    now = datetime.now()
    dt_string = now.strftime("%b-%d-%Y")

    if in_folder == "":
        newpath = folder + os.sep + dt_string
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    else:
        newpath = folder + os.sep + dt_string + os.sep + in_folder
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    i = 0
    while os.path.exists(newpath + os.sep + name + "%s" % i + "." + extension):
        i += 1

    filename = newpath + os.sep + name + "%s" % i + "." + extension

    return filename