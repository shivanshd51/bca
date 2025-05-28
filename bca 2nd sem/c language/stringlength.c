#include<stdio.h>
// int main(){
//     int i,count;
//     char str[50]="hello how are you";
//     for(i=0;str[i]!='\0';i++)
//     {
//     count++;
//     }
//     printf("%d",count);
// }

int main(){
    int i;
    char str1[500],str2[600];
    scanf("%s",str1);
    for(i=0;str1[i]!='\0';i++){
        str2[i]=str1[i];
    }
    str2[i]='\0';
    printf("%s",str2);
}