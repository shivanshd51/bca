#include<stdio.h>
#include<string.h>

struct address
{
    char city[20];
    int pin;
    char phone[14];
};

struct employee
{
    char name[20];
    struct address add;
};

int main(){
    struct employee emp;
    printf("enter employee information?\n");
    scanf("%s %s %d %s",emp.name,emp.add.city,&emp.add.pin,emp.add.phone);
    printf("printing employee information\n");
    printf("name:%s\ncity:%s\npincode:%d\nphone:%s",emp.name,emp.add.city,emp.add.pin,emp.add.phone);
    return 0;
}
    



