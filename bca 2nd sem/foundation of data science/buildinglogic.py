# 1.

# t=(1,2,3,4,5,6)
# a=len(t)
# l=[]
# for i in range(0,a-1):
#     b=t[i]*t[i+1]
#     l.append(b)

# print(tuple(l))


# 2.
# n=int(input("enter the number of element you want:"))
# l1=[]
# for j in range(n):
#     c=int(input("enter the element:"))
#     l1.append(c)

# t=tuple(l1)
# a=len(t)
# l=[]
# for i in range(0,a-1):
#     b=t[i]*t[i+1]
#     l.append(b)

# print(tuple(l))

3.

l=[{2:4,4:8},{"abc":1,"def":2,"ghi":3},{8:16,16:32}]
flag=0
a=len(l)
for i in range(0,a-1):
    if len(l[i])>len(l[i+1]):
        flag=i
    else:
        flag=i+1

print(l[flag],len(l[flag]))