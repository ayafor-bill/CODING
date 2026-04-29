#include <iostream>
using namespace std;



class Lecture{
    string hall;
    string state;
    string period;
    string time;
};

Lecture lecture1;
Lecture lecture2;
Lecture lecture3;

class Day{
    Lecture lecture[3] = {lecture1, lecture2, lecture3};
    string name;
}day1, day2;

Day day[2] = {day1, day2};
string classroom[3] = {"Hall1", "Hall2", "Hall3"};
string period[3] = {"period1", "period2", "period3"};


//functions to print the timetable:  /////////////////////////////////////
string word(string word) {
    return word;
}
string printl(Lecture thelecture) {
    word(thelecture.hall);
    word(thelecture.state);
    word(thelecture.period);
    word(thelecture.time);
}
string print(Day dotw){
    for(int i=0; i<3; i++) {
        cout<< dotw.name;
        printl(dotw.lecture[i]);
    }
}
/////////////////////////////////////////////////////////////////////////

//program to search for a day
void search() {
    string input;
    getline(input);

    if (input == day1.name) {
        print(day1);
    }
    else if(input == day1.name) {
        print(day2);
    }
    else {
        search();
    }
}

int main() {
    
    

    return 0;
}