# smallest number in list

a=[2,4,1,5,7,6]
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