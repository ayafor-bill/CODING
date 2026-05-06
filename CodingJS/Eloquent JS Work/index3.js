/*/Closure
function multiplier(factor){
    return number => number * factor;
}
let twice = multiplier(2)
console.log(twice(10));
*/
/* Exercises*/
/*/3.1 Minimum

function min(a,b){
    if(a > b){
       return a; 
    }
    else if(b > a){
        return b
    }
    else if(a == b){
    console.log("They are equal")
    }
}
console.log(min(5,90));
*/

/*/3.2 Recursion

function isEven(N){
    if(N == 0) return true;
    else if(N == 1) return false;
    else if(N < 0) return isEven(-N);
    else return isEven(N-2);
}
console.log(isEven(-1));
*/
//3.3 Bean Counting

function countBs(word){
    let count = 0;
    for(i = 0; i < word.length - 1; i++){
        if(word[i] == "B"){
           count ++; 
        }
    }
    return count;
}
console.log(countBs("BanBaBan"));

function countChar(string, ch){
    let count = 0;
    for(j = 0; j < string.length -1; j++){
        if(string[j] == ch){
            count ++;
        }
    }
    return count;
}
console.log(countChar("Autorenolaryngologist", "o"))
