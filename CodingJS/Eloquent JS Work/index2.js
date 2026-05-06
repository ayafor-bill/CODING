/**********  CHAPTER 2  **********/

// Functions
console.log(Math.max(5.3,3.0));         //Math.max() displays the highest number is a series of numbers and Math.min does the oposite

// Output all even numbers from zero to any
let num = 0, position = 1;
    while(position <= 12){
        console.log(num);
        num = num + 2;
        position = position + 1;
        }

// Supppose to keep asking for name if the user doesn't enter a name
/*
let yourName;
do{
    yourName = prompt("Who are you?");
}while(!yourName);
console.log("Hello" + yourName);
*/

/* EXERCISE */
//  1. Triangle of Hashes
/* let hash = "#", newHash = "#"
for(i = 1; i <= 7; i++){
    console.log(hash);
    hash = hash + newHash;
}*/

for(i = 0; i <= 7; i++){
    console.log('#'.repeat(i));
}

// Guess who's labor market just went up? THIS GUY!!!
for(i = 1; i <= 100; i++){ 
    if(i % 3 == 0 && i % 5 == 0){
        console.log("FizzBuzz");
    }
    else if(i % 3 == 0){
        console.log("Fizz");
    }
    else if(i % 5 == 0){
        console.log("Buzz");
    }
    else if(i == i){
    console.log(i);
    }    
}

// Remember your code didn't work so you checked the answer STUPID!!
let gridSize = 5;
let board = "";
for(i = 1; i <= gridSize; i++){
    for(j = 1; j <= gridSize; j++){
        if((i + j) % 2 == 0){
            board += " ";
        }else{
            board += "#";
        }
    }
    board += "\n";
}
console.log(board);



