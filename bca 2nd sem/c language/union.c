#include<stdio.h>
#include<string.h>

union emp
{
    int a;
    char b;
    float c;
    double d;
};

struct vlc
{
    int a;
    char b;
    float c;
    double d;
};

int main(){
    printf("%d\n",sizeof(union emp));
    printf("%d",sizeof(struct vlc));
    return 0;
}