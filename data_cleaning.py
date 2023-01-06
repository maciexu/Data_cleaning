# This is used to load datasets and do some repeatitive data cleaning as required. 
# Pre-cleaning is needed before load the data, like removing the extra cols and rows, etc.
# Final examination is also needed


import numpy as np
import pandas as pd

# Load the datasets (multisheets) and dataframe each sheet one by one
xls = pd.ExcelFile(r'path.xlsx')
df1 = pd.read_excel(xls, 'sheet1_name')

# exam the dataframe 
# print(df1.head())

# replace Yes to True and No to False
df1['col1'] = df1['Creditor List Available?'].replace(['Yes'], True)

# change the date to timestamp datetype. 
df1['Col_Date'] = df1['Col_Date'].values.astype(np.int64) // 10 ** 9

# print(df1['Col_Date'])

df1['Col1'] = df1['Col1'].apply(lambda x: "'" + str(x) + "'")
df1['Col2'] = df1['Col2'].apply(lambda x: "'" + str(x) + "'")
df1['Col3'] = df1['Col3'].apply(lambda x: "'" + str(x) + "'")
df1['Col4'] = df1['Col4'].apply(lambda x: "'" + str(x) + "'")

# IMPORTANT!!!!!!!! If Note is empty, otherwase use str(x), this needs to be fixed manually. 
df1['Note'] = df1['Note'].apply(lambda x: "'" + '' + "'")

df1['concat'] = df1.astype(str).fillna('').apply(', '.join, axis=1)

df1['concat'] = df1['concat'].apply(lambda x: "(" + str(x) + ")" + ",")

df1.to_excel("filings.xlsx", index=False) 

# End of the first sheet and then to insert into the DB.


# Sheet 2-5 should have 5 cols: name, filing, type, amount, current.
# if missing, please add blank cols manully ahead. 

df2 = pd.read_excel(xls, 'sheet2')
print(df2.head())

# replace ' to ''

# remove extra space and enter

# remove , in the amount col and besure it is float before concat. 

df2['name'] = df2['name'].apply(lambda x: "'" + str(x) + "'")
df2['filing'] = df2['filing'].apply(lambda x: "'" + str(x) + "'")
df2['Type'] = df2['Type'].apply(lambda x: "'" + str(x) + "'")

print (df2.head())

df2['concat'] = df2.astype(str).fillna('').apply(', '.join, axis=1)

df2['concat'] = df2['concat'].apply(lambda x: "(" + str(x) + ")" + ",")

# df2.Amount = df2.Amount.replace(np.nan, ' ', regex=True, inplace=True)
# not working, cannot replace nan to empty. Need to fix, otherwise fix manually. 



df2.to_excel("filing1.xlsx", index=False) 

