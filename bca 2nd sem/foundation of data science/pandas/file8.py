import pandas as pd
import numpy as np

data=pd.read_excel("Book1.xlsx")
k=data["total seat"]

l=0
for i in k:
	l=l+i

print(data.fillna("-",inplace=True))




#df=pd.DataFrame(data)
#data=np.array([1,2,3,4,5,6]).reshape(3,2)
#df=pd.DataFrame(data,index=["std1","std2","std2"]),column=["hindi","english"]
