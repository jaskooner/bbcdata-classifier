import pandas as pd 

dataset = "classifierdataset2.csv"
nRowsRead = 1000
df1 = pd.read_csv(dataset, delimiter=",", nrows = nRowsRead)
df1.dataframeName = " BBC news dataset"

nRow, nCol = df1.shape
print(f'There are {nRow} rows and {nCol} columns')

print(df1['labels'])
