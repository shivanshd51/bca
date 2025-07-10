#include<stdlib.h> 
#include <stdio.h> 

// creating and display node :-

void create(); 
void display(); 
void delete_beg();


struct node 
{ 
int info; 
struct node *next; 
}; 
struct node *start=NULL; 
int main() 
{ 
int choice; 
while(1){ 
printf("\n 1.Create \n"); 
printf("\n 2.Display \n"); 
printf("\n 3.Delete \n"); 

printf("Enter your choice:\t"); 
scanf("%d",&choice); 
switch(choice) 
{ 
case 1: 
create(); 
break; 
case 2: 
display(); 
break; 
case 3: 
delete_beg(); 
break; 
default: 
printf("\n Wrong Choice:n"); 
break; 
} 
} 
return 0; 
} 
void create() 
{ 
struct node *temp,*ptr; 
temp=(struct node *)malloc(sizeof(struct node)); 
printf("\nEnter the data value for the node:\t");      
scanf("%d",&temp->info); 
temp->next=NULL; 
if(start==NULL) 
{ 
start=temp; 
} 
else 
{ 
ptr=start; 
while(ptr->next!=NULL) 
{ 
ptr=ptr->next; 
} 
ptr->next=temp; 
} 
} 
void display() 
{ 
struct node *ptr; 
printf("\n The List elements are:\t"); 
for(ptr=start;ptr!=NULL;ptr=ptr->next) 
printf("%d \n",ptr->info );  }

void delete_beg() 
{ 
struct node *ptr; 
if(start==NULL){
    printf("list is empty");
}
else{
    ptr=start;
    start=start->next;
    free(ptr);
    return;
}
}