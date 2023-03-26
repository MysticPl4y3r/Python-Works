import pandas as pd

column=[]
table=pd.ExcelFile("BankProj.xlsx")
#xlread=pd.read_excel(table,sheet_name='Sheet1',skiprows=0,nrows=26)

for i in range(0,10):
    xlread=pd.read_excel(table,sheet_name='Sheet1',skiprows=i,nrows=26)
    column.append(xlread.columns[i])

print(column)