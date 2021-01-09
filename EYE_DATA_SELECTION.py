import os
import pandas as pd
import re

import csv


# get a look up table for selection
look_up = {}
with open ("no_add data_cleaned.csv") as csv_index:
    reader = csv.DictReader(csv_index)
    for row in reader:
        participant = row['Participant']
        NBack = row['NbackLevel']
        prefix = "frame number/"
        if int(participant) < 10:
            fileName = prefix + "P0" + str(participant) + "_" + str(NBack) + ".csv"
        else:
            fileName = prefix + "P" + str(participant) + "_" + str(NBack) + ".csv"
        look_up[fileName] = [row['Starting Frame Num'], row['Ending Frame Num']]

csv_index.close()

print('done')

#path of current directory
cwd = os.getcwd()

#dat = pd.read_csv(path, delim_whitespace=True)

# Find all txt file under current directory
f_path = []
d_name = []
for (dirpath, dirnames, filenames) in os.walk(cwd):
    f_name = dirpath.split(os.sep)[-1]
    if re.match(r"P\d\d_\d_FaceLab", f_name):
        d_name.append(f_name)
        for filename in filenames:
            # if Eye_ in file name then it is a txt file we want
            if re.match(r"Eye_.*\.txt",filename):
                # p is full path of txt files
                p = os.path.join(dirpath, filename)
                f_path.append(p)
        
    # Also need to collect the name of folders to use as stage number and participation number

# Read in first txt file
path = f_path[0]
final_dat = pd.read_csv(path, delim_whitespace=True)
# Add partipication number 
d = d_name[0]
p_number = d.split('_')[0][1:]
final_dat.insert(0, 'p_number', p_number)
# Add Stage number
stage = d.split('_')[1]
final_dat.insert(1, 'stage', stage)

# remove the first txt file
f_path = f_path[1:]
d_name = d_name[1:]
# Append the rest of the txt file to the first
for index,path in enumerate(f_path):
    dat = pd.read_csv(path, delim_whitespace=True)
    # Add partipication number 
    d = d_name[index]
    p_number = d.split('_')[0][1:]
    dat.insert(0, 'p_number', p_number)
    # Add Stage number
    stage = d.split('_')[1]
    dat.insert(1, 'stage', stage)
    # Connect dataframes
    final_dat = final_dat.append(dat)

# save dataframe as csv
final_dat.to_csv('data.csv', index=False)  



#print(dat.head(10)) 