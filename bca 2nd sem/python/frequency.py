a=int(input("enter the number of element you want:"))
l=[]
for i in range(0,a):
    b=int(input("enter the number:"))
    l.append(b)
t=tuple(l)
# print(t)

l2=[]
for j in t:
    c=t.count(j)
    d=(j,c)
    l2.append(d)
    

print(set(l2))