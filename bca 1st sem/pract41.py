print("choose your option \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Floor Division \n 6. Modulus")
a=int(input("enter the option :"))

def sum(x,y):
    return x+y

def dif(x,y):
    return x-y

def pro(x,y):
    return x*y

def div(x,y):
    return x/y

def fd(x,y):
    return x//y

def mod(x,y):
    return x%y

if a==1:
    i=int(input("enter the first number :"))
    j=int(input("enter the second number :"))
    print(sum(i,j))

if a==2:
    i=int(input("enter the first number :"))
    j=int(input("enter the second number :"))
    print(dif(i,j))

if a==3:
    i=int(input("enter the first number :"))
    j=int(input("enter the second number :"))
    print(pro(i,j))

if a==4:
    i=int(input("enter the first number :"))
    j=int(input("enter the second number :"))
    print(div(i,j))

if a==5:
    i=int(input("enter the first number :"))
    j=int(input("enter the second number :"))
    print(fd(i,j))

if a==6:
    i=int(input("enter the first number :"))
    j=int(input("enter the second number :"))
    print(mod(i,j))