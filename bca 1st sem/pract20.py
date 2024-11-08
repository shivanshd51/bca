x=[]
a=int(input('enter the number of elements you want :'))
i=0
while(i<a):
    b=int(input('enter the number you want to enter :'))
    x.append(b)
    i=i+1
print(x) 
d=int(input('enter the number you want to remove :'))
if(d in x):
    x.remove(d)
    print(x)
else:
    print('element is not in the list')