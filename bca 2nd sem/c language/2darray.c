#include<stdio.h>

int main(){
    int a[2][3],b[2][3],c[2][3],i,j;
    
    printf("first matrix\n");
    for(i=0;i<2;i++){
        for(j=0;j<3;j++){
            printf("enter the element:");
            scanf("%d",&a[i][j]);
        }
    }

    printf("second matrix\n");
    for(i=0;i<2;i++){
        for(j=0;j<3;j++){
            printf("enter the element:");
            scanf("%d",&b[i][j]);
        }
    }

    for(i=0;i<2;i++){
        for(j=0;j<3;j++){
            c[i][j]=a[i][j]+b[i][j];
        }
    }

    printf("sum of matrix\n");
    for(i=0;i<2;i++){
        printf("\n");
        for(j=0;j<3;j++){
            printf("%d ",c[i][j]);
            }
        }
    return 0;
}
