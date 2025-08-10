import numpy as np
ar1=np.array([[1,2,3,4],[4,3,2,1],[2,4,6,8]])
l=[]
for i in ar1:
	for j in i:
		l.append(j)

k=int(input("enter the number you want to check frequency:"))
b=l.count(k)		
print("frequency of",k,"is",b)