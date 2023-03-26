import pandas as pd

#write formulas
row=[[23,34,"=SUM(A2:B2)"],[10,5,"=SUM(A3:B3)"],[15,3,"=SUM(A4:B4)"]]
column=['A','B','Sum']

data=pd.DataFrame(data=row,columns=column)

with pd.ExcelWriter(r'Answer.xlsx') as writer:
    data.to_excel(writer,sheet_name="Solved",index=False)

#read formulas
f1=pd.read_excel(r"Answer.xlsx")

print(f1)