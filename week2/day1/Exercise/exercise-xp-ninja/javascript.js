// Exercise 1 : Find Nemo


// Ask the user to give you a sentence containing the word “Nemo”. 
//For example "I love the movie named Nemo !"
//let findNemo = prompt("Fill in a sentence with the word 'Nemo':");
// Find the word “Nemo”
// Console.log a string as follows: "I found Nemo at [the position of the word Nemo]!".
// Bonus : If you can’t find Nemo, console.log “I can’t find Nemo”.
// Hint : use an if/else statement

//if (findNemo.search("Nemo") > 0){
//    console.log("I found Nemo at", findNemo.search("Nemo"));
//}else {
//    console .log(" I can't find Nemo");
//}
// Some examples:

//     "I love the movie named Nemo !" ➞ "I found Nemo at 5"
//     "Nemo is a cute fish" ➞ "I found Nemo at 0"
//     "My fish is called Nemo, I love it" ➞ "I found Nemo at 4"
//***************************************************************************************

// Exercise 1 : Evaluation

//Evaluate the comparisons found below:
// 5 >= 1
//console.log(true)
// let x = 0;
// let y = 1;
// 0 === 1
// console.log(x === y); //false

// 4 <= 1
// let x = 4;
// let y = 1;
// console.log(x <= y); //false

// 1 != 1 //false
// let x = 1;
// console.log(x != x); //false

// "A" > "B"
// let x = "A";
// let y = "B";
// console.log(x > y); //false


// "B" < "C"
// let x = "B";
// let y = "C";
// console.log(x < y); //true

// "a" > "A"

// let x = "a";
// let y = "A";
// console.log(x > y); //true

// "b" < "A"
// let x = "b";
// let y = "A";
// console.log(x < y); //false

// true === false

// console.log(true === false); //false

// console.log(true != true)  //false
//************************************************* */

// Exercise 2 : Evaluation(2)
// Instructions
// Evaluate the code below. what would be the outcome if you run the code in the Javascript Console.
// Answer the questions below then check them line by line in the console.

//     let c;
//     let a = 34;
//     let b = 21;
//     a = 2;
//     a + b
// // What will be the outcome of a + b?
// console.log(a + b); //23
// // What is the value of c?
// console.log(c); /* undefined*/
// // Analyse the code below what will be the outcome?
// console.log(3 + 4 + '5'); //75
// *******************************************************************************************

// Exercise 3 : Ask For Numbers

// Instructions
// Ask the user for a string of numbers separated by commas, console.log the sum of the numbers.
// Hint: use some string methods

// Examples
// "2,3"➞ 5
// let strNum = prompt("please give a string of numbers separated by comma");


// function sumStr(strNum){
//     let strArr = strNum.split(",");
//     let sum = strArr.reduce(function(total, num){
//       return parseFloat(total) + parseFloat(num);
//     });

//     return sum;
// }

//**************************************************************************** */
// Exercise 4 : Boom


// Hint: if statement (tomorrow’s lesson)

// Prompt the user for a number. Depending on the users number you 
//will return a string of the word “Boom”. Follow the rules below:

// If the number given is less than 2 : return “boom”
// If the number given is bigger than 2 : the string should include n number of “o”s 
//(n being the number given)
// If the number given is evenly divisible by 2, add a exclamation mark to the end.
// If the number given is evenly divisible by 5, return the string in ALL CAPS.
// If the number given is evenly divisible by both 2 and 5, return the string in ALL CAPS and add an exclamation mark to the end.
// Examples
// 4 ➞ "Boooom!"
// // There are 4 "o"s and 4 is divisible by 2 (exclamation mark included)
// 1 ➞ "boom"
// // 1 is lower than 2, so we return "boom"


