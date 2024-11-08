# smallest number in list

a=[7,8,9]
i=0
b=0
c=a[0]
while(i<len(a)):
    b=a[i]
    if(b>c):
        b=c
    elif(c>b):
        b=b
    i=i+1
print(b)        