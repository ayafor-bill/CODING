#include <stdio.h>
#include <string.h>

int main() {
    int c, a;
    
    for(int i = 0; (c = getchar()) != EOF ; i++){
        c = a;
    for(int j = i; (a = getchar()) != EOF ; j--){
            putchar(a);
        }
    } 
        
    return 0;
}
