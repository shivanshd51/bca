#include<stdio.h>
#include<stdlib.h>


// 1. searching an element in array
// int main(){
//     int ar[6]={1,2,3,4,5,6};
//     printf("enter the value you want to search:");
//     int key;
//     int flag=0;
//     scanf("%d",&key);
//     for(int i=0;i<6;i++){
//         if(ar[i]==key){
//             flag=1;
//         }
//         else{
//             flag=flag;
//         }
//     }
//     if(flag==1){
//         printf("number is in the array");
//     }
//     else{
//         printf("number is not in the array");
//     }
// }

// 2.linked list

// void create(); 
// void display(); 
// void delete_begin();

// struct node 
// { 
// int info; 
// struct node *next; 
// }; 
// struct node *start=NULL; 
// int main() 
// { 
// int choice; 
// while(1){ 
// printf("\n 1.Create \n"); 
// printf("\n 2.Display \n"); 
// printf("\n 3. delete from beg \n"); 
// printf("Enter your choice:\t"); 
// scanf("%d",&choice); 
// switch(choice) 
// { 
// case 1: 
// create(); 
// break; 
// case 2: 
// display(); 
// break; 
// case 3: 
// delete_begin(); 
// break; 
// default: 
// printf("\n Wrong Choice:n"); 
// break; 
// } 
// } 
// return 0; 
// } 
// void create() 
// { 
// struct node *temp,*ptr; 
// temp=(struct node *)malloc(sizeof(struct node)); 
// printf("\nEnter the data value for the node:\t");      
// scanf("%d",&temp->info); 
// temp->next=NULL; 
// if(start==NULL) 
// { 
// start=temp; 
// } 
// else 
// { 
// ptr=start; 
// while(ptr->next!=NULL) 
// { 
// ptr=ptr->next; 
// } 
// ptr->next=temp; 
// } 
// } 
// void delete_begin() 
// { 
// struct node *ptr; 
// if(ptr==NULL) 
// { 
// printf("\n List is Empty:\n"); 
// return; 
// } 
// else 
// { 
// ptr=start; 
// start=start->next ; 
// printf("\n The deleted element is :%d ",ptr->info); 
// free(ptr); 
// } 
// } 
// void display() 
// { 
// struct node *ptr; 
// printf("\n The List elements are:\n\t"); 
// for(ptr=start;ptr!=NULL;ptr=ptr->next) 
// printf("%d \n",ptr->info );  
// } 


// 3.stack

// int stack[100],i,j,choice=0,n=4,top=-1;  
// void push(); void pop(); void show();  
// void main () 
// { 
// while(choice != 4) 
// { 
// printf("Chose one from the below options...\n");  
// printf("1.Push\n2.Pop\n3.Show");  
// printf("\n Enter your choice \n"); scanf("%d",&choice); 
// switch(choice) 
// { 
// case 1: 
// push(); break; 
// case 2: 
// pop(); break; 
// case 3: 
// show(); break; 
// default: 
// { 
// printf("Please Enter valid choice "); 
// } 
// } 
// } 
// } 
// void push () 
// { 
// int val; 
// if (top == n ) printf("\n Overflow");  
// else 
// { 
// printf("Enter the value?"); scanf("%d",&val); 
// top = top +1; stack[top] = val; 
// } 
// } 
// void pop () 
// { 
// if(top == -1) printf("Underflow");  
// else 
// top = top -1; 
// } 
// void show() 
// { 
// for (i=top;i>=0;i--) 
// { 
// printf("%d\n",stack[i]); 
// } 
// if(top == -1) 
// { 
// printf("Stack is empty"); 
// } 
// }

// 4.queue

// #define maxsize 5  
// void insert(); 
// void delete();
// void display(); 

// int front = -1, rear = -1; 
// int queue[maxsize];  
// void main () 
// { 
// int choice;
// while(choice != 4) 
// { 
// printf("\n1.insert an element\n2.Delete an element\n3.Display the queue\n");  
// printf("\nEnter your choice ?"); 
// scanf("%d",&choice);  
// switch(choice) 
// { 
// case 1: 
// insert(); break; case 2: 
// delete(); break; case 3: 
// display(); break;  
// default: 
// printf("\nEnter valid choice??\n"); 
// } 
// } 
// } 

// void insert() 
// { 
// int item; 
// printf("\nEnter the element\n"); 
// scanf("\n%d",&item); 

// if(rear == maxsize-1) 
// { 
// printf("\nOVERFLOW\n"); 
// return; 
// } 
// if(front == -1 && rear == -1) 
// { 
// front = 0; 
// rear = 0; 
// } 
// else 
// { 
// rear = rear+1; 
// } 
// queue[rear] = item; 
// printf("\nValue inserted "); 
// } 

// void delete() 
// { 
// int item; 
// if (front == -1 || front > rear) 
// { 
// printf("\nUNDERFLOW\n"); 
// return; 
// } 
// else 
// { 
// item = queue[front]; 
// if(front == rear) 
// { 
// front = -1; 
// rear = -1 ; 
// } 
// else 
// { 
// front = front + 1; 
// } 
// printf("\nvalue deleted "); 
// } 
// } 

// void display() 
// { 
// int i; 
// if(rear == -1) 
// { 
// printf("\nEmpty queue\n"); 
// } 
// else 
// { printf("\nprinting values \n");
// for(i=front;i<=rear;i++) 
// { 
// printf("\n%d\n",queue[i]); 
// } 
// } 
// } 

// stack using array

// int stack[100],i,n=4,top=-1,choice=0;

// void push();void pop();void show();

// void main(){
//     while(choice!=4){
//     printf("1.push\n2.pop\n3.show\nenter the choice:");
//     scanf("%d",&choice);
//     switch (choice)
//     {
//     case 1:
//     push();
//     break;
//     case 2:
//     pop();
//     break;
//     case 3:
//     show();
//     break;
//     default:
    
//     {
//         printf("enter the valid choice..");
//     }
//         break;
//     }
//     }

// }

// void push(){
//     if(top==n){
//         printf("overflow");
//     }
//     else{
//         int val;
//         top=top+1;
//         printf("enter the value:");
//         scanf("%d",&val);
//         stack[top]==val;
//     }
// }

// void pop(){
//     if(top==-1){
//         printf("underflow");
//     }
//     else{
//         top=top-1;  
//     }
// }

// void show(){
//     for(i=top;i>=0;i--){
//         printf("%d\n",stack[i]);
//     }
//     if(top==-1){
//         printf("empty stack");
//     }
// }