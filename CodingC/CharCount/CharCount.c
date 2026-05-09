#include<stdio.h>

int main()
{
    int c, n, to;
    while((c = getchar()) != EOF){
            ++n;
            if(c == 'to'){
             ++to;
            }
         putchar(c);
    }
        printf("There are %d characters and %d to", n, to);
    return 0;
}