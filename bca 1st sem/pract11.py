#sum of given numbers

a=int(input("enter a number :"))
b=0
while (not(a==0)):
    b=b+(a%10)
    a=a//10
    if(a==0):
        print("sum of the no. is",b)