import pandas as pd
f=("C:\CS\Python saves\BankProj.xlsx")
data=pd.read_excel(f)
print(data)

'''print(type(data)) #After importing, it is stored as DataFrame
print(data.head()) #shows first 5 rows
print(data.tail())  #shows last 5 rows
print(data.shape)   #prints dimensions of table from excel
print(data.sort_values(['Credit'],ascending=False))  #sort numerical values in ascending order
print(data.describe())   #shows table stats such as count,mean,max,etc
print(data['Credit'].mean())
data['Difference']=data['Credit']-data['Debit']
print(data['Difference'].head())'''

data.to_excel('Output.xlsx')#DataFrame is written to excel