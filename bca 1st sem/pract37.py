# take 2 set and print uncommon values in both the set
s1={1,2,3,4}
s2={3,4,5,6}

a=s1.intersection(s2)
b=s1.union(s2)

for i in a:
    b.remove(i)
print(b)    