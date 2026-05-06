/*/Exercise1
function revStr(word = ""){
    let rev = "";
    console.log("The word length is", word.length)
    for(i = word.length - 1; i >= 0; i--){
       rev += word[i];
    }
    return rev;
}
console.log(revStr("tather"));
*/
/*/Alg to select beans
1 - Put all beans in hand
2 - If bean is bad put in trash
3 - Repeat 2 until only good beans remain
4 - Put good beans in good bowl
*/
//Exercise2
arr = [1,2,1,3,4,2,1,1,4,6,3,4,3];
/*
const removeDupicates = (arr) => {
    let results = []

    for(let i = 0; i < arr.length; i++){
        if(!results.includes(arr[i])){
            results.push(arr[i])
        }
    }
    console.log(results)
}
removeDupicates(arr)
*/

//Exercise3
function deepEqual(val1, val2){
    if(val1 === val2){
        return true;
    }else return false;
}
let a1 = 2
let a2 = 2

console.log(deepEqual(a1, a2));