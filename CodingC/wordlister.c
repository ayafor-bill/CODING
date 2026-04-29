#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*int num_word(char word[], int num[]){
    
}*/

int main() {
    int pass;
    char pwd;
    int min;
    //int num[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    //char symbols[] = {'!', '@', '%', '&', '#'};
    
    //printf("How many words do you want to use: ");
    //scanf("%d", &wc);
    
    //char words[wc][20];
    
    //printf("\nEnter %d number of words: ", wc);
    
    /*for(int i = 0; i < wc; i++){
        printf("\n\tWord %d: ", i+1);
        scanf("%19s", words[i]);
    }*/
    printf("Enter max number of passwords: ");
    scanf("%d", &pass);
    
    printf("\nEnter length of password: ");
    scanf("%d", &min);
    
        
        for(int i = 0; i < pass; i ++){
            pwd = rand() % min;
            printf("%c\n", pwd);
        }
    
    return 0;
}