from cmath import nan
from email import header
import pandas as pd

df = pd.DataFrame({'a': [1,2,nan], 'b': [2,3,4], 'c':['dd','ee','ff'], 'd':[5,9,1]})

#df["rows_sum"] = df.sum(axis=0, skipna=True)

df1=pd.DataFrame({'A':[1,2,3,4]})
df2=pd.DataFrame({'A':[4,5,6]})

#dfc = df1[~df1.apply(tuple,1).isin(df2.apply(tuple,1))]

header = "a"

index = []
for i in df[header]:
    index.append(i)

print(index)

dfc = pd.concat([df1,df2]).drop_duplicates(keep=False)

