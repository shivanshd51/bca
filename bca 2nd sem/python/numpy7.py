import numpy as np
lst=[[[45,65,23],[87,3,6],[21,89,74],[1,2,3]]]
ar=np.array(lst)



"""
for x in np.nditer(ar):
	print(x)


print(ar)

print("dimension of array is:",ar.ndim,"dimension\n")

ar2=ar.reshape(2,6)
print(ar2)
print("dimension of array is:",ar2.ndim,"dimension\n")
"""

ar3=ar.reshape(12)
x=np.where(ar3%2==0)
print(x)
#print("dimension of array is:",ar3.ndim,"dimension\n")

