// practice set 1
#include<stdio.h>

// int main(){
//     int l,b,area;
//     printf("enter the lenght of rectange:");
//     scanf("%d",&l);
//     printf("enter the breadth of rectange:");
//     scanf("%d",&b);
//     printf("Area of rectangle: %d",l*b);
//     return 0;
// }


// int main(){
//     int r=6;    
//     int h=10;    
//     printf("the area of of circle with radius %d is %f",r, 3.14*r*r);
//     printf("the volume of of cylinder with radius %d and height %d is %f",r,h,3.14*r*r*h);
//     return 0;
// }



// practice set 2

// int main(){
//     int a=1;int b=a;  //correct//
//     int v=3*3; //correct//
//     // char dt='22 dec incorrect'
// }


int main(){
    int a= 97,b;
    printf("enter the number you want to check:");
    scanf("%d",&b);
    if(b%97==0){
        printf("%d is divisible by 97",b);
    }
    else{
        printf("%d is not divisible by 97",b);
    }
    return 0;
}