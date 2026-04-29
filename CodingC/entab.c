#include <stdio.h>

#define TAB_STOP 10

int main(){

    int c, col = 0, space = 0;

    printf("\nStart Typing\n");

    while((c = getchar()) != EOF){
        if(c == ' '){
            putchar(c);
            space++;
            col++
                if(col % space == 0){
                    putchar('\t');
                    space = 0;
                }
        }else {
            while(space > 0){
                putchar(' ');
                space--;
            }

            putchar(c);
            col++;

            if(c = '\n'){
                col = 0;
            }
        }
    }
    return 0;
}
*/
