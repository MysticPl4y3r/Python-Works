import pandas as pd

#Import excel table into python
excelfile=pd.ExcelFile(r"NewExcel.xlsx")
xlread=pd.read_excel(excelfile,sheet_name="Cars")
#print(xlread)

#Create table in python and export it to excel
#and reading table from one excel and exporting the same to another excel
data=[['Lamborghini','Aventador','Yes'],
     ['Koeningsegg','Jesko','No'],
     ['Audi','R8','Yes']]
columns=['Manufacturer','Model','Sold']
xlwrite=pd.DataFrame(data,columns)
xlwrite2=pd.DataFrame(xlread,columns=['Year'])
with pd.ExcelWriter("NewExcel.xlsx") as writer:
    xlwrite.to_excel(writer,sheet_name='Cars',index=False)
    #xlwrite2.to_excel(writer,sheet_name='Games',index=False)
#print(xlwrite2)'''



