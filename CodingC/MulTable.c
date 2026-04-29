#include <stdio.h>

int multip(int a){
    for(int i = 1; i <=12; i++){
        int b = a * i;
        printf("%d x %d = %d\n",a, i, b);
    }
}

int main() {
    int num;
      printf("Enter a number to print it's multiplication table: \n");
        scanf("%d", &num);
    
         multip(num);
    return 0;
}