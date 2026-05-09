#include <iostream>
using namespace std;

//1. First C program
/*int main() {
       cout << "Hello, World!";
    return 0;
}*/

//1. Value Swapper
int main(){
       cout << "Enter two numbers: " << endl;
       int n1 = 0, n2 = 0;
          cin >> n1 >> n2;
       
       int swap = (n2 + (n2=n1))-n1;
       
       cout << "Num1 = " << swap << " Num2 = " << n2 << endl;
}