#include<stdio.h>

struct employee
{
    int id;
    char name[20];
    struct date
    {
        int dd;
        int mm;
        int yyyy;
    }doj;
    
}e1;

int main(){

    e1.id=100;
    strcpy(e1.name,"shivansh");
    e1.doj.dd=7;
    e1.doj.mm=10;
    e1.doj.yyyy=2004;

    printf("%d %s %d %d %d",e1.id,e1.name,e1.doj.dd,e1.doj.mm,e1.doj.yyyy);

    return 0;
}

