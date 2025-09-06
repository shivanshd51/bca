#include<stdio.h>

int natural(int a){
    int b=0;
    for(int i=1;i<=a;i++){
        b = b+i;
    }
    printf("sum of %d natural numbers is %d",a,b);
}

int main(){
    natural(3);
    return 0;
}

