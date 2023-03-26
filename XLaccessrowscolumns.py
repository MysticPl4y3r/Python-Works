import pandas as pd

column=[]
row=[]
rows=[]

table=pd.ExcelFile("BankProj.xlsx")
xlread=pd.read_excel(table,sheet_name='Sheet1')

#Store columns in list
for i in range(0,xlread.shape[1]):
    column.append(xlread.columns[i])


#Store rows in list
for i in range(0,xlread.shape[0]):
    for j in range(0,10):
        row.append(xlread[column[j]][i])
    rows.append(row)
    row=[]

#print(xlread.columns[:])
for i in range(0,xlread.shape[1]):
    print(pd.Series(rows[i]))