# user defined dict

# using while loop
# d1={}
# a=int(input("enter the number of element :"))
# i=0
# while(i<a):
#     k=input("enter the key value :")
#     d=input("enter the data value :")
#     d1[k]=d
#     i=i+1
# print(d1)

# using for loop

d1={}
a=int(input("enter the number of element :"))
for i in range(0,a):
    k=input("enter the key value :")
    d=input("enter the data value :")
    d1[k]=d
print(d1)    