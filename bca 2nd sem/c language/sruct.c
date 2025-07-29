#include<stdio.h>
#include<string.h>
struct emoployee
{
    char name[100];
    int age;
}emp;

int main(){
    strcpy(emp.name,"shivansh");
    emp.age=20;

    printf("%d\n",emp.age);
    printf("%s",emp.name);
 
    return 0;
}