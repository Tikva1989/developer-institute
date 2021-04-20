//Exercise 1 : Change The Navbar

//1. In the <div> above, change the value of the id attribute from navBar to socialNetworkNavigation, 
//using the setAttribute method.

// let newDiv = document.getElementById("navBar");
// newDiv.setAttribute('id', 'socialNetworkNavigation');

// //2. We are going to add a new <li> to the <ul>.
//     // First, create a new <li> tag (use the createElement method).
//  // Create a new text node with “Logout” as its specified text.
//     // Append the text node to the newly created list node (li).
//     // Finally, append this updated list node to the unordered list above, 
//     //using the appendChild method.

//     function function1() {
//         var ul = document.getElementById("list");
//         var li = document.createElement("li");
//         li.appendChild(document.createTextNode("Logout"));
//         ul.appendChild(li);
//       }
//       function1("Logout")

// //3. Use the firstElementChild and the lastElementChild properties to 
// //retrieve the first and last li elements from their parent element (ul). 
// //Display the text of each link. (Hint: use the textContent property).

// let listUl = document.getElementById('list');
// console.log(listUl.lastElementChild.textContent);
// console.log(listUl.firstElementChild.textContent);


// ****************************

// // Exercise 2 : Users

// // In the HTML indexExercise2.html above change the name “Pete” to “Richard”.
//  1.  Create a new <li> element
// var user = document.createElement("li");
//     // console.log(user);
// //  2.  Create a new text node called "Richard"
// var textnode = document.createTextNode("Richard");
//     // console.log(textnode);
// //  3.  Append the text node to <li>
// user.appendChild(textnode);
//     // console.log(user.textContent);
// //  4.  Get the <ul> element with id="myList"
// var item = document.getElementById("myList");

// // //  5.  Replace the second child node (<li> with index 0) in <ul> with the newly created <li> element
// item.replaceChild(user, item.childNodes[1]);


// // // 2. Change each first name of the two <ul>'s to your name.

// var li_1 = document.getElementsByTagName("li")[0];
// var li_2 = document.getElementsByTagName("li")[2];
// li_1.textContent = "Tiki";
// li_2.textContent = "Tiki";

// ********************************************************************************

// Exercise 3:

// // For the following exercise use the HTML presented above:
// // Add a “light blue” background color and some padding to the <div>.
// var div = document.getElementsByTagName("div")[0];
// div.setAttribute("style", "background: lightBlue");
// div.style.padding ="10px";

// // Do not display the first name (John) in the list.
// var john = document.getElementsByTagName("ul")[0].getElementsByTagName("li")[0];
// var attr = document.createAttribute("hidden");
// john.setAttributeNode(attr);

// // Add a border to the second name (Pete).
// var pete = document.getElementsByTagName("ul")[0];
// var peteLis = document.getElementsByTagName("li")[1];
// peteLis.style.borderStyle = "solid";

// // Change the font size of the whole body.
// var body = document.body;
// body.style.fontSize = "30px";

// // Bonus: If the background color of the div is “light blue”,
// // alert “Hello x and y” (x and y are the users in the div).
// let x = document.getElementsByTagName("ul")[0].getElementsByTagName("li")[0].innerHTML;
// let y = document.getElementsByTagName("ul")[0].getElementsByTagName("li")[1].innerHTML;

// if (div.getAttribute("style").search(`background: lightBlue`)){
//         alert(`Hello ${x} and ${y}`);
// }