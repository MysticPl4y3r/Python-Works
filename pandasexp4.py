import seaborn as sns

ttnc=sns.load_dataset('titanic')

ttncIndex=ttnc.set_index(['class','who'])
print(ttncIndex.stack())
ttncind=ttnc.iloc[[0,1,2,3,4,5],[0,8]]
ttnccol=ttnc.loc[range(10),['sex','class','age']]
print(ttncind)
print(ttnccol)