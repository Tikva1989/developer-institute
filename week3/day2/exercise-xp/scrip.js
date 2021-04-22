// Exercise 1 : Change The Article

// //1. Using DOM methods, remove the last paragraph in the <article> tag from the DOM.
// let paraLast = document.getElementsByTagName("p")[3];
// paraLast.parentElement.removeChild(paraLast);

// // 2. Add an event listener which will change the 
// //background color of the h2 tag from the DOM when clicked on.

// let h2 = document.querySelector("h2");  //h2 location
// var attButton = document.createAttribute("button"); //new attribute 
// h2.setAttributeNode(attButton);                     //locate the attrButton in the element

// // add the event to the buttun in the element with relavent changes after clicked

// h2.addEventListener("click", function(){           
//     //  console.log("clicked");
//      h2.style.backgroundColor = "pink";
// });

// // 3. Set the font size of the h1 tag 
// //to a random pixel size between 0 to 100.(Check out this documentation)

// let h1 = document.querySelectorAll(" article h1")[0];
// var attH1 = document.createAttribute("button");
//  h1.setAttributeNode(attH1);       

//  h1.addEventListener("click",function(){
//     //   console.log("h1 clicked");
//      let newAttr=  document.createAttribute("style");
//      h1.setAttributeNode(newAttr);
//      var random = Math.floor(Math.random() * 101);
//     //  console.log(random);
//      newAttr.value = `font-size: ${random}px`;

//  });

// //4. Add an event listener which will hide the h3 when it’s clicked on 
// //(use the display property).
// var h3 = document.getElementsByTagName("h3")[0];
// h3.setAttribute("button", "");
// h3.addEventListener("click",function(){
//     h3.setAttribute("style", "display: none");
// });


// // 5. Add a <button> to the HTML file, that when clicked on, 
// // should make the text of all the paragraphs, bold.

// let btn = document.createElement("BUTTON", "type='button'");
// let btnText = document.createTextNode("click to bold");
// btn.appendChild(btnText);
// document.body.appendChild(btn);

// btn.addEventListener("click",function(){
//     document.body.style.fontWeight = "bold";
// });


//6.When the “Submit” button of the form is clicked:
// get the values of the input tags
// make sure that they are not empty, 
// then append them to a HTML table, in the div, below the form.

// let values = {
//     fname: '',
//     lname: ''
// }

// var addForm = document.forms[0]; var inputs = document.getElementsByTagName("input");
// for (input of inputs){
//     input.addEventListener("change", function(e){
//         values = {
//             ...values,
//             [e.target.name]: e.target.value
//         }
//         console.log(values);
//     })
// }

// addForm.addEventListener("submit", function(e){
//   e.preventDefault();

// })

// //7.  When you hoover on the 2nd paragraph, 
// //it should fade out (Check out “fade css animation” on Google)
// let para_2 = document.getElementsByTagName("p")[1];

// function fadeOutEffect() {
//     var para_2 = document.getElementsByTagName("p")[1];
//     var fadeEffect = setInterval(function(){
//         if (!para_2.style.opacity){
//             para_2.style.opacity -= 1;
//         }
//         if (para_2.style.opacity> 0){
//             para_2.style.opacity -= 0.1;
        
//         }else
//         clearInterval(fadeEffect);
//     }, 200);
// }
// para_2.addEventListener("mouseover", fadeOutEffect );