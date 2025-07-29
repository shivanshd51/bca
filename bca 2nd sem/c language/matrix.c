#include<stdio.h>

int main(){
    // transpose

    // int ar1[3][2];
    // int ar2[2][3];
    // int i,j;

    // for(i=0;i<3;i++){
    //     for(j=0;j<2;j++){
    //         printf("enter the element:");
    //         scanf("%d",&ar1[i][j]);
    //     }
    // }

    // printf("--matrix--\n");
    // for(i=0;i<3;i++){
    //     for(j=0;j<2;j++){
    //         printf("%d",ar1[i][j]);
    //     }
    //     printf("\n");
    // }
    // for(i=0;i<2;i++){
    //     for(j=0;j<3;j++){
    //         ar2[i][j]=ar1[j][i];
    //     }
    // }

    // printf("--matrix--\n");
    // for(i=0;i<2;i++){
    //     for(j=0;j<3;j++){
    //         printf("%d",ar2[i][j]);
    //     }
    //     printf("\n");
    // }
    // matrix multiplication

    int mat1[3][2];
    int mat2[2][3];
    int result[3][3];
    int i,j,k;

    for(i=0;i<3;i++){
        for(j=0;j<2;j++){
            printf("enter the element:");
            scanf("%d",&mat1[i][j]);
        }
    }
    for(i=0;i<2;i++){
        for(j=0;j<3;j++){
            printf("enter the element:");
            scanf("%d",&mat2[i][j]);
        }
    }

    printf("--matrix 1--\n");
    for(i=0;i<3;i++){
        for(j=0;j<2;j++){
            printf("%d",mat1[i][j]);
        }
        printf("\n");
    }
    printf("--matrix 2--\n");
    for(i=0;i<2;i++){
        for(j=0;j<3;j++){
            printf("%d",mat2[i][j]);
        }
        printf("\n");
    }

    // calculation

    int sum=0;
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            for(k=0;k<3;k++){
                sum+=mat1[i][k]*mat2[k][j];
            }
            result[i][j]=sum;
            sum=0;
        }
    }

    printf("--result--\n");
        for(i=0;i<2;i++){
        for(j=0;j<2;j++){
            printf("%d",result[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}