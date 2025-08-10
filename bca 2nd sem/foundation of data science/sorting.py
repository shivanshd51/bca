t=((1,"a"),(3,"c"),(2,"b"))
l=[]
for i in t:
    a=i[0]
    l.append(a)

l2=[]
b=sorted(l)
for j in l:
    s=str(j)
    for k in t:
        r=str(k)
        if s in r:
            l2.append(r)


print(l2)




    
    # print(i)