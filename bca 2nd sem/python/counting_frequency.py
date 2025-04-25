a=input("enter the number you want to check:")
count=0
for i in range(1,101):
    b=str(i)
    if a in b:
        count=count+1
print(count)