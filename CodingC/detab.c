#include <stdio.h>

#define TAB_STOP 10

int main(){

    int c;

    printf("Start Typing\n");

    for(int i = 0; (c = getchar()) != EOF; i++){
        if(c == '\t'){
            for(int j = 0; j < TAB_STOP - (i % TAB_STOP); j++){
                putchar(' ');
                i++;
            }
        } else {
            putchar(c);
        }
    }
    return 0;
}
