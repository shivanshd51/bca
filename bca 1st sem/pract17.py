# a=[1,2,3]
# a.insert(0,0)
# print(a)

# user defined element insertion
a=[1,2,3]
print(a)
b=int(input("enter the position you want to enter the element :"))
c=int(input("enter the value of the element :"))
a.insert((b-1),c)
print(a)