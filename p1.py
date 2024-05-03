import pandas as pd
import numpy as np

# t=(1,8,100,10)
# l=[1,8,100,10]
# d={1,8,100,10}
# h="Hello"
# a=np.arange(6)
# s=pd.Series(h)

# print(s)

ser=pd.Series(data=[5,8,10,None],index=["a","b","b","c"],name="python")
# print(ser)
# print(ser.index)
# print(ser.values)
# print(ser.dtype)
# print(ser.shape)
# print(ser.dtype.itemsize)
# print(ser.size)
# print(ser.nbytes)
# print(ser.hasnans)
# print(ser.empty)
# print(ser.count())
# print(len(ser))
# print(ser.ndim)
# print(ser.name)
# print(ser.sort_index)
# print(ser.sort_values)
# print(ser.is_unique)

# ser1=ser[0:2]
# ser1[0:2]=100
# print(ser[ser>5])


# s=pd.Series(data=range(5),index=["A","B","C","D","E"])
# print(s)
# print(s[0:2])
# print(s["D"])
# # print(s["D","E"])
# print(s[["D","E"]])

# data = { 'name' : ['AA', 'IBM', 'GOOG'],
# 'date' : ['2001-12-01', '2012-02-10', '2010-04-09'],
# 'shares' : [100, 30, 90],
# 'price' : [12.3, 10.3, 32.2]
# }
# s=pd.DataFrame(data)
# s["newData"]=[1,2,3]
# s.index=["a","b",'c']

# print(s["shares"])
# df = pd.read_csv('data.csv')
# print(df)


df= pd.read_csv('auto-mpg.csv')
# df = pd.read_csv("https://raw.githubusercontent.com/patelmanishv/Sem4Data/main/auto-mpg.csv")
# print(df.to_string())
# print(ser)
# print(ser.index)
# print(ser.values)
# # print(ser.dtype)
# print(ser.shape)
# # print(ser.dtype.itemsize)
# print(ser.size)
# # print(ser.nbytes)
# # print(ser.hasnans)
# print(ser.empty)
# print(ser.count())
# print(len(ser))
# print(ser.ndim)
# # print(ser.name)
# print(ser.sort_index)
# print(ser.sort_values)
# print(ser.is_unique)


# print(df.head(10))
# print()
# print(df.tail(5))

# print(df.info())
# print(df.describe())

df=pd.read_csv("AXISBANK.csv")
print(df)
print()
print(df.head(10))
print()
print(df.tail(10))
print()
print(df.info())
print()
print(df.describe())#statistics
print()
print(df["Volume"])