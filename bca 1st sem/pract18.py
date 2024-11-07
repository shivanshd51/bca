# user defined list with square of entered element
a=[]
i=0
c=int(input("enter the number of element you want in list :"))
while(i<c):
    b=int(input("enter the number you want to enter :"))
    a.append(b**2)
    i=i+1
print(a)    