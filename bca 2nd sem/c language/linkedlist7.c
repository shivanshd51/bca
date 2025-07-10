#include<stdio.h>
#include<stdlib.h>

struct Node {
    int data;          
    struct Node* next;
};

struct Node newNode(int data) {
    struct Node* temp = 
      (struct Node*)malloc(sizeof(struct Node));
    temp->data = data;
    temp->next = NULL;
    
}

int main(){
    
    return 0;
}