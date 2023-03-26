import pandas as pd

quant=[30,28,13,23]
model=['Audi TT','Bentley Continental GT','BMW M3 E92','Ferrari LaFerrari']
year=[2019,2010,2010,2018]

cD=pd.DataFrame({'Model':model,'Year':year,'Quantity':quant})
eD=pd.DataFrame({'S.no':[1,2,3,4,5],'name':['Alex','David','Hudson','Woods','Yuri']})
cD2=pd.DataFrame({'Model':['Lamborghini Aventador','Ferrari LaFerrari','BMW M3 E92','Audi TT'],'Sales':[180,500,275,310],'Engine':['V12','V12','V8','V10']})
cD3=pd.DataFrame({'Model':['Lamborghini Aventador','Ferrari LaFerrari','BMW M3 E92','Audi TT'],'Top Speed(km/h)':[340,340,290,293],'Engine Placement':['Mid engine','Mid engine','Front Engine','Front Engine']})
print(cD)
print(cD2)
print(cD3)
#Only tables with common column can be merged
#and even if there is common column there must be common rows in common column as well
print('Merged DataFrames :')

df=pd.merge(cD,cD2) #Can merge two tables at a time
print(df)

df2=pd.merge(df,cD3)
print(df2)

df2.to_excel('CarDetails.xlsx')