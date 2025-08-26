import pandas as pd
d=pd.DataFrame({'student':["aditya","saksham","suryansh"],'roll_no':["101","102","103"]})
print(d.loc[0]['student'])