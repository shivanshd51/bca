# checking the number is palindrome or not

a=int(input("enter the number you want to check :"))
x=a
i=0
while(a>0):
    i=i*10+a%10
    a=a//10
if x==i:
    print("number is palindrome..")
else:
    print("number is not palindrome..")    