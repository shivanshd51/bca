#include<stdio.h>
#include<string.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
};

int main(){
    struct node *head=NULL;
    head=(struct node *)malloc(sizeof(struct node));
    head->data=10;
    head->next=NULL;
    
    printf("data:%d",head->data);

}

void insert(){

}