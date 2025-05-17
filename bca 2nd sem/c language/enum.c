#include<stdio.h>

enum weekdays{
    sunday=15,
    monday,
    tuesday,
    wednesday,
    thursday,
    friday,
    saturday
};

int main(){
enum weekdays w;
w=saturday;
printf("the value of w is:%d",w);
return 0;
}