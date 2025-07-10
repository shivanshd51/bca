#include<stdio.h>
#include<stdlib.h>

void create();
void display();

struct node{
    int info;
    struct node *next;
};

struct node *start=NULL;
int main(){
    int choice;
    while(1){
        printf("\n 1.Create");
        printf("\n 2.Display");
        printf("\n Enter your Choice:\t");
        scanf("%d",&choice);
        switch(choice){
            case 1:
            create();
            break;
            case 2:
            display();
            break;
            default:
            printf("\n Wrong Choice:");
            break;
        }
    }
    return 0;
}

void create(){
    struct node *temp,*ptr;
    temp=(struct node*)malloc(sizeof(struct node));

    printf("\nEnter the data value for the node:\t");
    scanf("%d",&temp->info);
    temp->next=NULL;
    if(start==NULL){
        start=temp;
    }
    else{
        ptr=start;
        while(ptr->next!=NULL){
            ptr=ptr->next;
        }
        ptr->next=temp;
    }
}

void display(){
    struct node *ptr;

    printf("\nthe list elements are:");
    for(ptr=start;ptr!=NULL;ptr=ptr->next){
    printf("%d\n",ptr->info);}
}