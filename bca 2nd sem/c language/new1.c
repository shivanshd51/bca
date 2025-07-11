#include<stdio.h>
#include<stdlib.h>


int a,b,c;

int sum(int a,int b){
    c=a+b;
    return c;
}

int main(){
    int x=sum(3,4);
    printf("%d",x);
    return 0;
}