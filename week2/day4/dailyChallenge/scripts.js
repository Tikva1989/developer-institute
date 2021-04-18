
/*Find the longest word in the array for the fram*/

function longestWord(array) {
    let longest = 0;
    for (let word of array) {
        // console.log(word);
        if (word.length > longest) {
            longest = word.length;
        }
    }
    return longest;
}

//The actual execution

let sentance = prompt(""); //to add prompt at the end
sentance_array = sentance.split(" "); /*turn string to an array*/

const longest = longestWord(sentance_array); /*in this case is 5- frame size */
const border = new Array(longest + 5).join("*");  // set te upper+lower border

console.log(border);
for (let word of sentance_array) {
    console.log("* " + word + new Array(longest - word.length + 1).join(" ") + " *"); //make a new array for the spaces
}
console.log(border);





// **************
// style a console log output:

const spacing = '10px'; 
const styles =  `padding: ${spacing}; background-color: Black; color: white; border: 1px solid black; font-size: 2em;`;

// console.log('%', styles);
// ***********************************