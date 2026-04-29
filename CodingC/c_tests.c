#include <stdio.h>

int main(){
    int a, c, i = 0;
    //char ch[100];

    while((c = getchar()) != EOF){
        if(c == '/'){
            a = getchar();
            printf("\nThis is the comment: ", putchar(a));
        }
        else{
            putchar(c);
        }
   
    }

    return 0;
}