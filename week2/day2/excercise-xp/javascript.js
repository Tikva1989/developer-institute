// Exercise 1: Simple If/Else Statement
// Instructions
// Create 2 variables, x and y. Each of them should have a different numeric value.
// Write an if/else statement that checks which number is bigger.


// let x = 1;
// let y = 2;

/*  if (x > y) {
    console.log("x is the biggest number");
} else {
    console.log("y is the biggest number");
} */

//***************************************************************************** */

// Exercise 2: Chihuahua

// Create a variable called newDog where it’s value is “Chihuahua”.
// let newDog = "Chihuahua";

// Check and display how many letters are in newDog.
// console.log(newDog.length);

// Display the newDog variable in uppercase and then in lowercase 
// (no need to create new variables, just console.log twice).
// console.log(newDog.toUpperCase());
// console.log(newDog.toLowerCase());

// Check if the variable newDog is equal to “Chihuahua”
// if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
// else, console.log ‘I dont care, I prefer cats’
/*
if (newDog == prompt("")) {
    console.log("I love Chihuahuas, it’s my favorite dog breed");
} else {
    console.log("I dont care, I prefer cats");
}
*********************************************************************************************/
// Exercise 3: Even Or Odd
/* Prompt the user for a number and save it to a variable*/

// let x = parseInt(prompt("Enter a number"));

/* Check whether the variable is even or odd.
If it is even, display: “x is an even number”. Where x is the actual number the user chose.
If it is odd, display: “x is an odd number”. Where x is the actual number the user chose.*/


// if (x % 2){
//     console.log("x is an odd number");
// }else {
//     console.log("x is an even number");
// }
//************************************************************************************ 
 //Exercise 4 : Switch Case

// let whatHappens;
// let direction;

// switch (direction) {
//     case "forward":
//         break;
//         whatHappens = "you encounter a monster";
//     case "back":
//         whatHappens = "you arrived home";
//         break;
//         break;
//     case "right":
//         whatHappens = "you found a river";
//         break;
//     case "left":
//         break;
//         whatHappens = "you run into a troll";
//         break;
//     default:
//         whatHappens = "please enter a valid direction";
// }

// /What is the value of the whatHappens variable, 
//when the value of the direction variable is “forward”

//console.log("you encounter a monster");
//______________________________________________________
// What is the value of the whatHappens variable, 
//when the value of the direction variable is “back”

//console.log("you arrived home");
//_________________________________________________________
//What is the value of the whatHappens variable, 
//when the value of the direction variable is “right”

//console.log("you found a river");
//_______________________________________________________
//What is the value of the whatHappens variable, 
//when the value of the direction variable is “left”

//console.log("you run into a troll");
//************************************************************************************* */

//Exercise 5: Group Chat

let users = ["Lea123", "Princess45","cat&doglovers", "helooo@000"]

// //If there is no users (the users array is empty), console.log “no one is online”.
// If there is 1 user, console.log “<name_user> is online”.
// If there are 2 users, console.log “<name_user1> and <name_user2> are online”.
// If there are more than 2 users, console.log the first two names in the users array and the number of additional users online.
// For example, if there are 5 users, it should display:

if (users.length == 0){
    console.log("no one is online");
} else if (users.length == 1){
    console.log(users[0], "is online");
} else if (users.length == 2){
    console.log(users[0],  users[1], "are online");
} else{ 
    console.log( users[0], users[1], (users.length-2), "more are online" );
}
