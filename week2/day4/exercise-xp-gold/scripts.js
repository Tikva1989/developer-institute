// Exercise 1 : Is_Blank

// Write a program to check whether a string is blank or not.

// function is_Blank(str){
//     if (str === ""){
//         return true;
//     } else {
//         return false;
//     }
// }
// console.log(is_Blank(''));
// console.log(is_Blank('abc'));

// **************************************************************

// Exercise 2 : Abbrev_name

// Write a JavaScript function to convert a string into an abbreviated form.

// function abbrev_name(str1){
//     let str1Array = str1.trim().split(" ");
//     if (str1Array.length > 1){
//         return (str1Array[0] + " "+ str1Array[1].charAt(0) +".");
//     }
//     return str1Array[0];
// }
// console.log(abbrev_name("Robin Singh"));

// *********************************************************************

// Exercise 3 : SwapCase

// Write a JavaScript function which takes a string as an argument and swaps the case of each character.
// For example :

// if you input 'The Quick Brown Fox' 
// the output should be 'tHE qUICK bROWN fOX'.

// var str = "The Quick Brown Fox";
// const UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
// const LOWER = 'abcdefghijklmnopqrstuvwxyz';
// var result = [];

//   for(var x=0; x<str.length; x++)
//   {
//     if(UPPER.includes(str[x]))
//     {
//       result.push(str[x].toLowerCase());
//     }
//     else if(LOWER.includes(str[x]))
//     {
//       result.push(str[x].toUpperCase());
//     }
//     else 
//     {
//       result.push(str[x]);
//     }

//   }

// console.log(result.join(''));

// function swapCase(str) {
//     const upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
//     const lower = 'abcdefghijklmnopqrstuvwxyz';
//     let resultSwap = [];
//     for (i = 0; i < str.length; i++) {
//         if (upper.includes(str[i])) {
//             resultSwap.push(str[i].toLowerCase());
//         } else if (lower.includes(str[i])) {
//             resultSwap.push(str[i].toUpperCase());
//         } else {
//             resultSwap.push(str[i]);
//         }
//     }
//     return resultSwap.join("");
// }
// ************************************************************************

// Exercise 4 : Omnipresent Value

// Create a function that determines whether an argument is omnipresent for a given array.
// A value is omnipresent if it exists in every subarray inside the main array.

// let bigArray = [[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]];

//enter element store in array's array:
// console.log(bigArray[0][0]);

function isOmnipresent (bigArray, omniValue){
    for (i=0;i<bigArray.length;i++){
               if( bigArray[i].includes(omniValue)){
                   return true
               }else {
                   return false
               }
                
            }
    
    }

console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1));
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6));
console.log(isOmnipresent([[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]], 3));
