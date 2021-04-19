var currentNumber = [] ; ///will store the current number
var privuosNumber ; //will store the first num for any expression
var operstion ;     // 
var result = 0 ;//how's the cal works;


function number(num){
   currentNumber.push(num);
   console.log(num) ; // logs the digit presset for the current number 
   console.log(currentNumber);
}



function operator(operator){
    privuosNumber = parseInt(currentNumber.join(''));
    currentNumber= [];          //reser the current number to add more numbers if needed
    console.log(privuosNumber); //the firs number typed showed as a join string
    // console.log(typeof(privuosNumber));
   operstion = operator;
    
}

function equal() {
    
    currentNumber = parseInt(currentNumber.join(''));
    
    if ( operator === '+') {
        eval (currentNumber + privuosNumber);
    } else if (operator === '-') {
        console.log(currentNumber - privuosNumber)
    } else if (operator === '*') {
        console.log(currentNumber * privuosNumber)
    } else {
        console.log(currentNumber / privuosNumber)
    } 
}