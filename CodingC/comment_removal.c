#include <stdio.h>

#define LINE_BUFFER 1000
#define COM_BUFFER 500

int col = 1;
//Count the number of lines in the code
int count_lines(int lc){
    int line_count = 0;
        if(lc == '\n'){
            line_count++;
        }
    return line_count;
}

//Check for comment and store in a buffer
int com_check(int caract){
    char com_buffer[COM_BUFFER];
    int com_index = 0;
    if(caract == '/'){
        caract = getchar();

    }
    putchar(caract);
}

int main(){
    int c, cm;
    char line_buffer[LINE_BUFFER];
    int line_index = 0;

//Entering the Program
    printf("\n|---------- COMMENT REMOVER ----------|\n");

    printf("\nEnter your program: ");

//Tracking each Line
    while((c = getchar()) != EOF){
        line_buffer[line_index++] = c;
        col++;

        com_check(c);

//Stopping the current line and analyzing the next
        if(c == '\n'){
            int restart_line = 0;
            line_buffer[restart_line++] = c;
            com_check;
        }
        putchar(c);
    }

    return 0;
}
