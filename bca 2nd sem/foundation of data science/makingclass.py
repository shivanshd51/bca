class employee:
    def details(emp):
        emp.name=input("enter the name of emp:")
        emp.id=int(input("enter the id of emp:"))
        emp.desi=input("enter the designation  of emp:")
        emp.salary=int(input("enter the basic salary of emp:"))
        ta=(emp.salary/100)*2.5
        da=(emp.salary/100)*1.5
        emp.tsalary=emp.salary + ta + da

    def display(emp):
        print("emp name:",emp.name)
        print("emp id:",emp.id)
        print("emp designation:",emp.desi)
        print("emp salary:",emp.salary)
        print("emp total salary:",emp.tsalary)

a=employee()
a.details()
a.display()

b=employee()
b.details()
b.display()