import pandas as pd
from os import listdir
from os.path import isfile, join


def remove_N_rows(csv_file,n_rows):
    data = pd.read_csv(csv_file, sep=',', skiprows = n_rows)
    return data

mypath = '../sources/Air_source/csv/'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

master_df  = []
file_number = 0
for file in files:
    path = '../sources/Air_source/csv/' + file
    if file_number == 0:
        master_df = remove_N_rows(path,4)
    else:
        master_df = pd.merge(master_df,remove_N_rows(path,4),how='outer')
        #master_df = pd.concat([master_df,remove_N_rows(path,5)])
    file_number = 1
    #print(master_df.head())

master_df.to_csv('../sources/Air_source/csv/covid19_totalDB_clean.csv', index=False)
print(master_df.head())
print(master_df.info())
print(master_df.describe())
