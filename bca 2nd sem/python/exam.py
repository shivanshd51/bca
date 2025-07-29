import pandas as pd
data=[(1,"shivansh",12),
      (2,"shivam",13),
      (3,"vivek",14),
      (4,"suryansh",15)]
df=pd.DataFrame(data,columns=("S.no","name","roll no."))
print(df)