d1={}
a=int(input("enter the number of element"))
for i in range(0,a):
    k=input("enter the key value :")
    d=input("enter the data value :")
    d1[k]=d
l=[]
for x in d1:
    l.append(x)
print(sorted(l))    