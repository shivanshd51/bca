# 1.	Write a python program to count the number of even and odd numbers from a series of numbers given by user.

# a=int(input("enter the number of element you want to enter :" ))
# b=[]
# for i in range(1,a+1):
#     b.append(i)

# even=0
# odd=0
# for j in b:
#     if j%2==0:
#         even= even+1
#     else:
#         odd= odd+1

# print("No. of even number :",even)
# print("No. of odd number :",odd)

# 2.  Write a program to print cube of a number given by user.

# a=int(input("enter the number of cube you want :"))
# print(a**3)


# 3.	Write a program to take the percentage of a student and prints its grade according to below criteria: -
# Grade A greater than 90, 
# Grade B greater than 80, 
# Grade C greater than 70, 
# Grade D greater than 60, 
# Grade E greater than 50, 
# Grade F less than 50

# a=float(input("enter the percentage of student :"))
# if (a>=90):
#     print("student's grade is A")
# elif (a>=80):
#     print("student's grade is B")
# elif (a>=70):
#     print("student's grade is C")
# elif (a>=60):
#     print("student's grade is D")
# elif (a>=50):
#     print("student's grade is E")
# elif (a<50):
#     print("student's grade is F")
# else:
#     print("enter valid data..!")    

#4.	Write a program to print the multiplication of three numbers given by user.

# a=int(input("enter the first number :"))
# b=int(input("enter the second number :"))
# c=int(input("enter the third number :"))
# print(a*b*c)

#7.	Write a program to print first 10 natural numbers by using while loop.

# i=1
# while(i<11):
#     print(i)
#     i=i+1

#8.	Write a program to print squares of first 100 natural numbers.

# for i in range(1,101):
#     print(i**2)

#9.	Write a program to accept three different numbers from user and find which is greater.

# a=int(input("enter the first number :"))
# b=int(input("enter the second number :"))
# c=int(input("enter the third number :"))

# if(a>b>c):
#     print(a,"is the greatest number")
# elif(b>c>a):
#     print(b,"is the greatest number")
# else:
#     print(c,"is the greatest number")

# 18

# a=int(input("Enter the value you want table of :"))
# for i in range(1,11):
#     print(a*i)

#first factorial of a number through recursive function

# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return (x * factorial(x-1))
    
# print(factorial(5))


# l=[]
# for i in range(0,5):
#     b=int(input("enter element"))
#     l.append(b)

# # print(sum(l))
# c=len(l)
# for k in l:
#     z=(k,l.count(k))
#     print(set(z))


# print("maximum number is :",max(l))
# print("minimum number is :",min(l))

# a=int(input("enter the number you want table of :"))
# for i in range(1,11):
#     print(a*i)

# 16.	Write a program to create a user defined list of 5 elements and perform following operations on that list: -
# l=[]
# for i in range(0,5):
#     b=int(input("enter the element:"))
#     l.append(b)
# print("user defined list:",l)

# # a)	Sum of all numbers	
# print("sum of all five elements:",sum(l))

# # b) count frequency of each number
# dict={}
# for j in l:
#     dict[j]=(l.count(j))
# print("frequency of elements:",dict) 

# 8 write a program to check prime number

# a=int(input("enter the number you want to check :"))
# b=False

# if(a==0 or a==1):
#     print("print number is not prime")

# else:
#     for i in range(2,a):
#         if a%i==0:
#             b=True
#         else:
#             b=b
    
#     if b:
#         print("number is not prime")
#     else:
#         print("number is prime")



# sum of n natural number

# def sum(x):
#     if x==1:
#         return 1
#     else:
#         return(x+sum(x-1))

# print(sum(int(input("enter the nth term :"))))

# 3.Write a program to take different words separated by comma and print reverse 
# order of their occurrence.

# a=input("enter the words separated by commas:")
# b=a.split(",")
# b.reverse()
# print(b)

# 2.	Write a program to print Fibonacci series for first 20 terms

a=int(input("enter number :"))
print("fibonacci sequence:")
n1=0
n2=1
i=0
while(i<a):
    print(n1)
    print(n1+n2)
    n1=n2
    i=i+1

# 1.	Write a python program to calculate electricity bill according to given criteria: 
# 1 - 100 unit - 1.5/= 
# 101-200 unit - 2.5/= 
# 201-300 unit - 4/= 
# Above 300 unit - 10/=

# a=int(input("enter the unit :"))
# if (a>=100):
#     d=a*1.5
#     print("Your Bill is:", d)
# elif (100<a>=200):
#     print("Your Bill is:", a*2.5)
# elif (200<a>=300):
#     print("Your Bill is:", a*4)
# elif (a>300):
#     print("Your Bill is:", a*10)
# else:
#     print("enter valid data..")

# a=int(input("enter the nth term:"))
# l=[]
# for i in range(1,a+1):
#     b=i**3
#     l.append(b)
# print(l)
    

# a=int(input("enter the unit:"))
# if(a<100):
#     print("Your electricity bill is:",a*1.5)
# elif(100<a<=200):
#     print("Your electricity bill is:",a*2.5)
# elif(200<a<=300):
#     print("Your electricity bill is:",a*4)
# elif(a>300):
#     print("Your electricity bill is:",a*10)
# else:
#     print("enter valid data")
