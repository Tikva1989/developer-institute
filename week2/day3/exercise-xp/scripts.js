// Exercise 1 : Your Favorite Colors
// Instructions
// // Create an array called colors where the value is a list of your favorite colors.
// color = ["Blue ", "Green", "Red", "Orange", "black", "Yellow "];
// // Loop through the array and as you loop console.
// //log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
// // Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// // Hint : create an array of suffixes to do the Bonus
// o = ["th","st","nd","rd"]

// function Ordinal(n)
//  {
//  var o = ["th","st","nd","rd"],
//  x = n%100;
//  return x+(o[(x-20)%10]||o[x]||o[0]);
//  }

// for(n = 0; n < color.length; n++){
//  var ordinal = n + 1;

//  var output = (Ordinal(ordinal) + " choice is " + color[n] + ".");

// console.log(output);
// }

// ********************************************************************************************

// Exercise 2 : List Of People
// Instructions
// var people = ["Greg", "Mary", "Devon", "James"]
// Write code to remove “Greg” from the people array.




// people.shift("Greg");
// // Write code to replace “James” to “Jason”.

// // Write code to add your name to the end of the people array.
// people.push("Tiki");
// // Using a loop, iterate through the people array and console.log each person.

// for(let i =0; i< people.length; i++){
//     console.log(people[i]);
// }

// // Using a loop, iterate through the people array and after you console.log
// // “Jason” exit the loop.

// for(let i =0; i< people.length; i++){
//     if(i > 2){
//         break;
//     }
//     console.log(people[i]);
// }
// Write code to make a copy of the people array using slice. 
//The copy should NOT include “Mary” or your name.

// let newPeople = people.slice(2);

// Write code that console.logs Mary’s index. take a look at indexOf on google.

// people.indexOf("Mary");

// Write code that gives the indexOf “Foo” (this should return -1). 
//Why does it return -1

// console.log(people.indexOf("Foo"));

/* "Foo" is't found on the list of people array.*/

// Create a variable called last which value is the last element of the array.

// let last = people[people.length-1];
// console.log(last);

// ****************************************************************************************************
// Exercise 3 : Repeat The Question
// Instructions
// Prompt the user for a number, while the number is smaller 
//than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?
// Hint : Check the data type you receive from the prompt (ie. typeof method)

// let num = parseInt(prompt("Enter number"));

 
// do {
//     parseInt(prompt("Enter number"));
    
//   }
//   while (num > 10);

// ********************************************************************************************
// Exercise 4 : Attendance

// let guestList = {
//   randy: "Germany",
//   karla: "France",
//   wendy: "Japan",
//   norman: "England",
//   sam: "Argentina"
// };

// // Given the object above where the key is the students name and the value is the country
// // they are from.

// // Prompt the student for their name :
// // If the name is in the object, console.log the name of the student and the country 
// //they come from.
// // example: "Hi! I'm [name], and I'm from [country]."
// // Hint: Look up the statement if ... in
// // If the name is not in the object, console.log: "Hi! I'm a guest."


// // using for...in
// for ( let key in guestList ) {

//     // display the properties
//     console.log(`"Hi! I'm" ${key}, "and i'm from"${guestList[key]}`);
// } 
// *****************************************************************************

// Exercise 5 : Family
// Instructions
// Create an object called family with a few key value pairs.
// Console.log the keys. (using a for loop).
// Console.log the values. (using a for loop).
let family = {
    dad: "Danni",
    mom: "Shani",
    bigBrother: "Dolev",   
    sister : "Shoahana," 
};

var x;
for (x in family) {
  family[x];
}
console.log(x)