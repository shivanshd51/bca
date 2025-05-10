#include<stdio.h>

int main(){
    int a[4];
    int i,j;
    for(i=0;i<4;i++){
        printf("enter the element:");
        scanf("%d",&a[i]);
    }

    // for(i;i<4;i++){
    //     printf("%d",a[i]);
    // }
    for(j=0;j<4;j++){
    printf("%d\n",a[j]);
    }
    return 0;
    }