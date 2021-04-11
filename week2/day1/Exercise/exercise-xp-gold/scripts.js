//Exercise 1 : Favorite Color
//let me = ["my","favorite","color","is","blue"]

let me = ["my", "favorite", "color", "is", "blue"];
console.log(me);

// Exercise 2 : Mixup
//Create 2 variables. The values should be strings. For example:
let str1 = "mix";
let str2 = "pod";

//Slice out and swap the first 2 characters of
// the 2 strings from part 1 : 
//example 1:

let newStr1 = str2[0] + str1[1] + str1[2];
let newStr2 = str1[0] + str2[1] + str2[2];
let newWord = newStr1 + " " + newStr2;
// example 2:

let firstWord = "Hello";
let secondWord = "World";
let firstWord1 = firstWord.substring(0, 4) + secondWord[4];
let secondWord1 = secondWord.substring(0, 4) + firstWord[4];
let thirdWord = secondWord1 + " " + firstWord1;



//Exercise 3 : Calculator
let num1 = prompt("Enter first number for sum", null);
let num2 = prompt("Enter second number for sum", null);
let sum = parseInt(num1) + parseInt(num2);
alert(sum);

//BONUS: Make a program that can subtract
let num3 = prompt("Enter first number for subtract", null);
let num4 = prompt("Enter second number for subtract", null);
let subtract = parseInt(num3) - parseInt(num4);
alert(subtract);

// multiply: 
let num5 = prompt("Enter first number multipy", null);
let num6 = prompt("Enter second number multipy", null);
let multiply = parseInt(num5) * parseInt(num6);
alert(multiply);

//divide:
let num7 = prompt("Enter first number for divide", null);
let num8 = prompt("Enter second number for divide", null);
let divide = parseInt(num7) / parseInt(num8);
alert(divide);
