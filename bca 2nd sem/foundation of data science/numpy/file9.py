import numpy as np
ar=np.array([[1,2,3,4,5]])
l=[]
for i in ar:
	for j in i:
		b=j**2
		l.append(b)

ar2=np.array([l])

print(ar2)