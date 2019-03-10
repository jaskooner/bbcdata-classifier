import os
import pandas as pd 

nRowsRead = 1000
df1 = pd.read_csv("bbc-dataset.csv", delimiter=",", nrows = nRowsRead)
df1.dataframeName = " BBC news dataset"

nRow, nCol = df1.shape
print(f'There are {nRow} rows and {nCol} columns')

print(df1['description'])

