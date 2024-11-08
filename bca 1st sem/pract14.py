# greatest number in the list

a=[-5,-3,-8]
i=0
b=a[i+1]
c=len(a)
while(i<c):
    d=a[i]
    if(b>d):
        b=b
    elif(d>b):
        b=d
    i=i+1    
print(b)    

    