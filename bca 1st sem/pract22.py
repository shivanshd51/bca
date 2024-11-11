a=[[[2,3,4]],[[6,5,8]]]

# using for loop

# for i in a:
#     for j in i:
#         for k in j:
#             print(k)

# using while loop

i=0
while(i<2):
    j=0
    while(j<1):
        k=0
        while(k<3):
            print(a[i][j][k])
            k=k+1
        j=j+1    
    i=i+1  