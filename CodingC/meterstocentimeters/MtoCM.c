#include<stdio.h>
#include<math.h>

int main(){
float a;
printf("Enter the length in metre: \n");
scanf("%f", &a);

float b = a*100;

printf("\n%.3fm in centimeters is %.3fcm", a, b);

   return 0;
}