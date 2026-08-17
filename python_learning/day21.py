import pandas as pd
# s=pd.Series([10,20,30,40])
# print(s)
# s=pd.Series([10,20,30],index=["python","sql","django"])
# print(s)
# print(s.dtype)
# s=pd.Series([10,20,30,40],name="Marks")
# print(s)
# dataframe
# data={
#     "name":["rakesh","anjali","diksha"],
#     "age":[10,20,30],
#     "marks":[20,60,50]

# }
# df=pd.DataFrame(data)
# print(df)
# print(df.shape)
# print(len(df))
# print(df.size)
# print(df.tail(1))
# print(df.head)
# print(df.columns)
# print(df.index)
# data={
#     "name":["rakesh","anjali","diksha"],
#     "age":[10,20,30],
#     "marks":[20,60,50]

# }
# df=pd.DataFrame(data)
# print(df[["name","marks"]])
# print(df.iloc[0])
# print(df.loc[1,"name"])
# print(df["marks"]>20)
# print(df["name"].str.startswith("r"))
# df["name"]="diksha"
# print(df)
# print(df.age.isna())
df=pd.read_csv("python_learning/student.csv")
print(df)
print(df.head())
print(df.info())
# print(df.shape())