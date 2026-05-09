#include <stdio.h>
#include <string.h>

/*int to_num(char alph[], char base[]){
    char result, finres;
    for(int i = 0; i < 9; i++){
      result = (alph[i] * base[9 - i]);
    }
    finres = result + to_num(alph[9], base[35]);
    
    return finres;
}
*/

int main() {
    char alnum[9];
    char base[35] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
    
        printf("Enter alphqnumeric number: ");
        scanf("%s", &alnum);
    
    for(int i = 0; i < 9; i++){
        printf("%d", alnum[i]);
    }
    return 0;
}