# greatest number in the list

a=[2,1,3,5,8,9]
i=0
b=0
c=len(a)
d=0
while(i<c):
    d=a[i]
    if(b>d):
        b=b
    elif(d>b):
        b=d
    i=i+1    
print(b)    

    