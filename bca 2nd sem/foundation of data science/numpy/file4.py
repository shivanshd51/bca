import numpy as np
ar1=np.array([[1,2,3,4],[4,3,2,1],[2,4,6,8]])

even=[]
odd=[]

for i in ar1:
	for j in i:
		if j%2==0:
			even.append(j)
		else:
			odd.append(j)
			
print("even numbers:",np.array(even))
print("odd numbers:",np.array(odd))


