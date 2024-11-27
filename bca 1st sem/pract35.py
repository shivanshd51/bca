d1={}
a=int(input("enter the number of element :"))
for i in range(0,a):
    k=input("enter the key value :")
    d=input("enter the key value :")
    d1[k]=d
print(d1)

l1=[]
for j in d1.values():
    l1.append(j)

for k in l1:
    print(k,"=",l1.count(k))