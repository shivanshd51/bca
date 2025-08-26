import pandas as pd

d={
"students":["suryansh","aditya","raj","karan","mayank","aryan","saksham","ram","shyam","ajay"],
"roll no":[101,102,103,104,105,106,107,108,109,110],
"age":[18,19,20,19,18,17,20,19,21,18],
"marks":[85,88,75,86,90,85,88,75,86,98],
"course":["bca","ds","ds","bca","ds","bca","ds","ds","bca","ds"]}

df1=pd.DataFrame(d)
print(df1.describe())