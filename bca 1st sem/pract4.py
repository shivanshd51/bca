day=int(input("enter the number:"))
a=day%7
if(a==1):
    print("monday")
elif(a==2):
    print("tuesday")    
elif(a==3):
    print("wednesday")    
elif(a==4):
    print("thursday")    
elif(a==5):
    print("friday")    
elif(a==6):
    print("saturday")    
elif(a==0):
    print("sunday")    
else:
    print("enter a valid data")