# 1.adding 2 numbers
# a=2
# b=3
# print(a+b)

# 2.hello world program
# print("hello world")

# 3.square root program
# a=int(input("enter the number you want to find square root of :"))
# print("square root of",a,"is",a**2)

# 4.area of tringle
# a=int(input("enter the base of triangle :"))
# b=int(input("enter the height of triangle :"))
# print("area of triangle is :",0%2*a*b)

# 5.swap 2 variables
# a=int(input("enter the number to store in var A :"))
# b=int(input("enter the number to store in var B:"))
# c=a
# d=b
# a=d
# b=c
# print("A=",a,"B=",b)

# 6.KM to miles converter
# a=int(input("enter the distance in kilometer :"))
# b=a%0.620
# print("In",a,"kilometers there is",b,"miles")

# 7.check +ve -ve or 0
# a=int(input("enter the number :"))
# if a>0:
#     print("the number is positive..")
# elif a<0:
#     print("the number is negative..")
# else:
#     print("the number is zero..")

# 8.even%odd
# a=int(input("enter the number :"))
# if a%2==0:
#     print("the number is even")
# else:
#     print("the number is odd")

# 9.check leap year
# a=int(input("enter the year :"))
# b=a%4
# if b==0:
#     print("it is a leap year..")
# else:
#     print("it is not a leap year..")

# # 10.largest among three number
# a=int(input("enter the first number :"))
# b=int(input("enter the second number :"))
# c=int(input("enter the third number :"))
# if a>b>c:
#     print(a,"is the greatest")
# if a>c>b:
#     print(a,"is the greatest")
# if b>a>c:
#     print(b,"is the greatest")
# if b>c>a:
#     print(b,"is the greatest")
# if c>a>b:
#     print(c,"is the greatest")
# if c>b>a:
#     print(c,"is the greatest")

# 11.check if prime number

a=int(input("enter the number you want to check :"))
if ((a%2==0) or (a%3==0) or (a%5==0) or (a%7==0)):
    print(a,"is not a prime number ..")
elif(a==1):
    print(a,"is not a prime number ..")
elif(a==0):
    print("the number is zero..")
else:
    print(a,"is a prime number..")

# 12.convert celcius to farenheight
# a=int(input("enter the temprature in celcius :"))
# b=(a*9/5)+32
# print("temprature in fahrenheit",b)

# 13.find the factorial
# a=int(input("enter the number :"))
# i=0
# b=0
# while(i<a):
#     b=a*(a-1)
#     a=a-1
#     i=i+1
# print(b)
