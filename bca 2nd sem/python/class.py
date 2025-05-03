class course:
    cn=input("a)BSC(Bio) b) BSC(Maths)\nEnter your choice (a/b):")

    def __init__(self):
        if self.cn=="a":
            print(["COURSE: BSC(Bio)","DURATION: 3year"])
        elif self.cn=="b":
            print(["COURSE: BSC(Maths)","DURATION: 4year"])
        else:
            print("enter the valid choice..")

class student(course):
    sn=input("enter the full name of student:")
    p=int(input("enter the marks of physics:"))
    c=int(input("enter the marks of chemisrty:"))
    e=int(input("enter the marks of english:"))
    def __init__(self):
        course()
        tt=((self.p)+(self.c)+(self.e))/3
        print(self.sn)
        print(tt)

student()