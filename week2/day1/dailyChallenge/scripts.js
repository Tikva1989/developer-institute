//console.log("my daily challenge");
// Exercise 1:
let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

// Remove Banana from the array
fruits.splice(0, 1);

// Sort the array in alphabetical order
fruits.sort();

//Add “Kiwi” to the end of the array
fruits.push("Kiwi");

// Remove “Apples” from the array. Don’t use the same method as in part 1

delete fruits[1];

// Sort the array in reverse order. (Not alphabetical, but reverse the current Array
//  i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])

let reversFruites = fruits.reverse();

// Exercise 2:

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1][0]);