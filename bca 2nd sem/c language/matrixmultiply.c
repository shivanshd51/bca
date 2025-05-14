#include<stdio.h>

int main(){
    int a[2][3],b[3][2],r[2][2],i,j,k,sum=0;

    printf("-first matrix-\n");
    for(i=0;i<2;i++){
        for(j=0;j<2;j++){
            printf("enter the element:");
            scanf("%d",a[i][j]);
        }
    }

    printf("-second matrix-\n");
    for(i=0;i<2;i++)
    {
        for(j=0;j<2;j++)
        {
            printf("enter the element:");
            scanf("%d",b[i][j]);
        }
    }

    printf("-resultant matrix-\n");
    for(i=0;i<2;i++)
    {
        for(j=0;j<2;j++)
        {
            for(k=0;k<3;k++)
            {
                sum+=a[i][k]*b[k][j];
            }
            r[i][j]=sum;
            sum=0; 
        }
    }

    return 0;
}