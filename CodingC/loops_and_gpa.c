#include <stdio.h>
#include <stdlib.h>

int main() {
    int NoC;
    
    //banner
         printf("Fill in the following\n");
        
    //Number of courses        
         printf("\nNumber of Courses: ");
         scanf("%d", &NoC);
        
    //Get Courses, Course credit and score
        
   char courses[NoC][30];
   float score[NoC];
   int credit[NoC];
   int colmn = 30;  
        
        if(NoC > 0){
         for(int i = 0; i < NoC; i++){
              //Name   
                 printf("\n\t%-21s:   ","Course Name");
                 scanf(" %[^\n]", courses[i]);
              //Credit   
                 printf("\t%-22s:   ", "Course Credit");
                 scanf("%d", &credit[i]);
              //score
                 printf("\t%-28s:   ", "Score");
                 scanf("%f", &score[i]);
         }
        }
     
     //Table
     
     // Print table header
            printf("\n\n%-30s | %-20s | %-10s", "Course Name", "Credit Value", "Score");
            printf("\n----------------------------------------------");

     // Print each course's details
        for (int a = 0; a < NoC; a++) {
            printf("\n%-37s | %-20d | %-10.1f", courses[a], credit[a], score[a]);
         }
     
          return 0;
}