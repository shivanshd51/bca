a=int(input("enter the multidigit number :"))
k=a
j=0
while k!=0:
    j=j*10+(k%10)
    k=k//10
print(j)