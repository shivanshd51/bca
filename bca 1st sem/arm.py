def armstrong(n):
    sum=0
    b=len(n)
    for i in n:
        sum+=int(i)**b
    if sum==int(n):
        print("armstrong")
    else:
        print("not an armstrong")

a=input("enter the number you want to check:")
armstrong(a)