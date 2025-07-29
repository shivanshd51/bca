int stack[100],i,n=4,top=-1,choice=0;

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