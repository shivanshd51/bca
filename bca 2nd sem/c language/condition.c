#include<stdio.h>
// greatest of tow numbers
int main(){
    int a,b;
    printf("enter the first number:");
    scanf("%d",&a);
    printf("enter the second number:");
    scanf("%d",&b);
    if(a>b){
        printf("the greater number is :%d",a);
    }
    else{
        printf("the greater number is :%d",b);
    }
}