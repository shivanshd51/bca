a=int(input("enter the number to check :"))
x=a
l=[]
while x!=0:
    i=x%10
    l.append(i)
    x=x//10
l.reverse()

b=len(l)
z=0
for i in l:
    z=z+(i**b)

if a==z:
    print(a,"is armstrong number")
else:
    print(a,"is not armstrong number")

# a="SHIVANSH"
# print(a.center(a))