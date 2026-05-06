function grade(mark){

    let grade = {
        excellent : 'A',
        pass : 'B',
        average : 'C',
        belowAverage : 'D',
        fail : 'F',
    };
     if(mark >= 90 <= 100){
        console.log(grade.excellent);
     }
     else if(mark >= 80 <= 89){
        console.log(grade.pass)
     }
     else if(mark >= 70 <= 79){
        console.log(grade.average)
     }
     else if(mark >= 60 <= 69){
        console.log(grade.belowAverage)
     }
     else if(mark >= 0 <= 59){
        console.log(grade.fail)
     }
}
console.log(grade(90))