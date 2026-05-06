//*******    CHAPTER 1     *******/
//------INTRODUCTION------//

//Learning to print with different variable types
var name = 'Afesi Ayafor Bill Adib';
let age = 17;
    console.log('My name is', name, 'and i am', age, 'years old');

//Learning simple operations
let total = 0, count = 1;
while(count <= 10) {
    total += count;
    count += 1;
}
console.log(total);

//Applying new knowledge on different variable types
let greet = 'Hello there!!';
let rep = 1;
while(rep <= 10){
    console.log(rep+'.', greet);
    rep += 1;
}

//Factorial Program
function factorial(n){
    if (n == 0){
        return 1;
    } else {
        return factorial(n - 1) * n;
    }
}
console.log(factorial(8));

//Values
let nonsense = 0/0;

console.log(nonsense);

console.log(typeof nonsense);

//escaping characters & template literals
console.log("This is the first line\nThis is the second");
console.log("A newline character is written like \"\\n\".");

console.log(`Half of 100 is ${100/2}`);

//Boolean & Conditional operators
console.log(1<5);
console.log(10 * 10 > 20 && 1 - 2 == -1);
console.log(true ? 1 : 2);
console.log(false ? 1 : 2);

