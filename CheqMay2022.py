import csv




FILENAME = "CheqMay2022.csv"

import pandas as pd
df = pd.read_csv('CheqMay2022.csv', header=None)
df.rename(columns={0: 'Date', 1: 'Amount'}, inplace=True)
df.to_csv('test_with_col.csv', index=False) # save to new csv file

def write_info(info):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(info)

def read_info():
    info = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            info.append(row)
    return info


test = read_info()

for i, test in enumerate(test, start=1):
        print(f"{i}. {test[0]} {test[1]} {test[4]}")
        print()