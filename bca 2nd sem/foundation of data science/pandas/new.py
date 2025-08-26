import pandas as pd
import numpy as np

"""df=pd.read_excel("fdsBook2.xlsx")

print(df.fillna("missing"))
print(df.fillna(method="ffill"))
print(df.fillna(method="bfill"))
print(df)
print(df.drop_duplicates())

df1=pd.read_excel("fdsBook1.xlsx")
df2=pd.read_excel("fdsBook2.xlsx")

#print(df1)
#print(df2)

#x=pd.concat([df1,df2],axis=1)
#x=pd.merge(df1,df2,on="course",how="left")
#x=pd.merge(df1,df2,on="course",how="right")
#x=pd.merge(df1,df2,on="course",how="inner")
x=pd.merge(df1,df2,on="course",how="outer")
print(x)
"""

#--group by--1:41 PM 7/1/2025

df5=pd.read_excel("fdsBook3.xlsx")
#print(dir(df5))

#a=(df5.groupby("Course"))
#print(a.min())
#print(a.max())
#print(a.size())
#print(a.describe())
#print(a.count())
#print(a.first())
#print(a.last())
#print(a.nth(1))

#--QUESTION 3:08 PM 7/2/2025--

#print(a.get_group("BCA"))

"""for x,y in a:
	print(x,y) #where x gives group name and y gives group member"""


"""print("average",a.agg({'Marks':'mean'}))
print("minimum",a.agg({'Marks':'min'}))
print("maximum",a.agg({'Marks':'max'}))

print(a.agg(['min','max']))
"""

df4=pd.read_excel("fdsBook4.xlsx")


#Que1--> Replace missing value with the column mean.

'''sov=df4['marks'].sum()
tv=df4['marks'].count()
mean=(sov/tv)
x=df4.fillna(mean,inplace=True)
print(df4)
'''

#--Homework 14:52 03-07-2025--
#Que2--filter top scoring student who got marks more than or equal to 75--

a=df4.groupby("marks")
if 


#Que3--remove age column from filtered data frame--

x=df4.pop("age")
print(df4)


#Que4--adding one column last name and one more column full name which combine both column--










