import pandas as pd

excelfile=pd.ExcelFile("Functions.xlsx")
xlread=pd.read_excel(excelfile,sheet_name="Sheet1")
print(xlread[1:])