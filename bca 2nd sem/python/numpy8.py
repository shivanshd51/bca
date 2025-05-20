import numpy as np

ar1=np.array([[45,65],[23,34]])
ar2=np.array([[21,89],[74,24]])
print("first array\n",ar1)
print("second array\n",ar2)

ar3=np.concatenate((ar1,ar2),axis=1)
print("result array\n",ar3)