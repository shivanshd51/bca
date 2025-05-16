#include<stdio.h>

// user defined multiply function

int multiply(int a,int b){
    return a*b;
}

int main(){
    int c,d;
    printf("enter the first number:");
    scanf("%d",&c);
    printf("enter the second number:");
    scanf("%d",&d);
    printf("product of both the numbers:%d",multiply(c,d));
    return 0;
}