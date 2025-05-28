#include<stdio.h>

// int main(void){
//     char name[]="harry potter";
//     printf("%c\n",name);
//     printf("%c\n",*name);
//     printf("%c\n",*(name+1));
//     printf("%c\n",*(name+7));
//     return 0;
// }

int main(){
    char *arr[4]={"c++","python","c","r"};
    int n=sizeof(arr)/sizeof(arr[0]);
    printf("array elements:\n");
    for(int i=0;i<n;i++){
        printf("%s\n",arr[i]);

    }

    return 0;
}