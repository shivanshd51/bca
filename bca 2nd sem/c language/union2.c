#include<stdio.h>

union abc
{
    int a;
    char b;
};


int main(){
    union abc *ptr;
    union abc var;
    var.a=90;
    var.b=50;
    ptr=&var;
    printf("the value of a is:%d",ptr->a);
    return 0;
}