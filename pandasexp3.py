import numpy as np, pandas as pd

carquant={"Audi":30,"Bentley":28,"BMW":13,"Ferrari":np.nan}
carModel={"Audi":"TT","Bentley":np.nan,"BMW":"M3","Ferrari":"LaFerrari"}
carYear={"Audi":2019,"Bentley":2010,"BMW":2019,"Ferrari":2018}

#quant=pd.Series(carquant)
quant=[30,28,13,23]
#model=pd.Series(carModel)
model=['Audi TT','Bentley Continental GT','BMW M3 E92','Ferrari LaFerrari']
#year=pd.Series(carYear)
year=[2019,2010,2019,2018]

carDetails=pd.DataFrame({'Model':model,'Year':year,'Quantity':quant})
empDetails=pd.DataFrame({'S.no':[1,2,3,4,5],'name':['Alex','David','Feron','Hudson','Woods']})
carDetails2=pd.DataFrame({'Model':['Lamborghini Aventador','Ferrari LaFerrari','BMW M3 E92','Audi TT'],'Sales':[180,500,275,310],'Engine':['V12','V12','V8','V10']})

print(carDetails)
print(carDetails2)

print('Merged DataFrames :')

df=pd.merge(carDetails,carDetails2)
print(df)

'''print('\n')
print("Index of car details :",carDetails.index,'\n')
print("Columns of car details :",carDetails.columns)
print('\n')
print(carDetails['Model'])''' 

#print(carDetails.isnull())
'''print(carDetails.notnull())
print(carDetails.dropna())
print("\n")
print(carDetails.dropna(axis=1))
print('\n')
print(carDetails.dropna(axis=1,how='any'))
print('\n')
print(carDetails.dropna(axis=0,thresh=1))'''
carDetails.interpolate(method='linear',limit_direction='backward')

#df=pd.DataFrame({'date':pd.date_range(start='2022-07-01',periods=10,freq='h'),
#                 'value':range(10)})
#print(df)
