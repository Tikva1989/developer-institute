// Exercise 1 : Keyless Car
// Instructions
// Ask the user for their age, and save the value to a variable.


// Create a function called checkDriverAge() that will notify the user 
//if they are permitted to drive. They must be at least 18 to drive.
// if the user is too young, alert “Sorry, you are too young to drive this car. Powering off”
// if the user is old enough, alert “You are old enough to drive, Powering On. Enjoy the ride!”
// if the user just turned 18, alert “Congratulations on your first year of driving. Enjoy the ride!”

// let myAge= +prompt("What is your age?");

// function checkDriverAge(myAge) { 
//     if (myAge < 18){
//     alert("Sorry, you are too young to drive this car. Powering off");
//     }else if (myAge> 18){
//       alert("You are old enough to drive, Powering On. Enjoy the ride!");
//     } else if (myAge = 18) {
//         alert("Congratulations on your first year of driving. Enjoy the ride!");
//     }
// }

// checkDriverAge(myAge);

// Instead of using prompt to ask the user for their age, have the checkDriverAge() function 
//accept an argument age.


// function checkDriverAge(myAge) {   
//     if (myAge < 18){
//       console.log("Sorry, you are too young to drive this car. Powering off");
//     }else if (myAge> 18){
//        console.log("You are old enough to drive, Powering On. Enjoy the ride!");
//     } else if (myAge = 18) {
//         console.log("Congratulations on your first year of driving. Enjoy the ride!");
//     }
// }

// checkDriverAge(50);

// **************************************************************************************************

// Exercise 2 : What’s In My Wallet ?

// Instructions
// Given a item price and an array representing the amount of change in your pocket, 
//determine whether or not you can afford the item.
// Change will always be represented in the following order: quarters, dimes, nickels, pennies.



// let coin = [0.25, 0.10, 0.05, 0.01];
// function changeEnough(change, itemCost) {
//     var sum = 0;
//     for (let i = 0; i < change.length; i++) {
//         sum += change[i] * coin[i];
//     } 
//     if (sum >= itemCost) {
//         console.log(true);
//     } else {
//         console.log(false);
//     }
// }
// //To illustrate:
// changeEnough([2, 0, 20, 100], 1.00);
// changeEnough([2, 100, 0, 0], 14.11);
// changeEnough([0, 0, 20, 5], 0.75);

// ******************************************************************************

// Exercise 3: Find The Multiples Of 23
// Instructions
// Write a js function that 
//console.logs all multiples of 23 less than 500, at the end return the sum of all the multiples.

// var sum = 0;
// for (var x = 0; x <= 500; x++)
// {
//     if (x % 23 === 0 )
//     {
//        sum += x;
//     }
// }
// console.log(sum);
// ***********************************************************************************

// Exercise 4 : Amazon Shopping
// Instructions
// let amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100,
// }
// Create a function called checkBasket().
// It should:
// prompt the user for an item
// let the user know if the item is in the basket
// Hint: Use the in keyword inside the conditional


// function checkBasket(basket) {
//     let item = prompt("Item to check in basket:").toLocaleLowerCase();
//        if(item in basket) {
//        console.log(item + " is in your basket");
//        }   else { 
//         console.log(item + " is not in your basket");
//         }
// }
// checkBasket(amazonBasket);

// ****************************************************************
// Exercise 5 : Shopping List
// Instructions
// let stock = {
//     "banana": 6,
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry": 1
// }

// let prices = {
//     "banana": 4,
//     "apple": 2,
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry": 10
// }
// Add the stock and prices objects to your js file.
// Create an array called shoppingList with the following items:
// “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.

// let shoppingList = ["banana","orange", "apple" ];
// 
// Create a function called myBill() that takes no arguments.
// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock.
// If the item is in stock find out the price in the prices object.
// Call the myBill() function.
// Bonus: If the item is in stock, decrease the item’s stock by 1


// function myBill() {
//     let totalSum = 0;

//     for (item of shoppingList) {
//         if (item == stock[item] && stock[item]>0) {
//           totalSum += prices[item];
//         }
//     }
//     return totalSum
// }

// myBill(shoppingList);

// **********************************************************************************************
// Exercise 6 : Tips

// John created a simple tip calculator to help calculate how much to tip when he 
//and his family go to restaurants.

// The calculator has the following rules:
// 1. Tip 20% when the bill is less than $50,
// 2. Tip 15% when the bill is between $50 and $200,
// 3. Tip 10% if the bill is more than $200.

// Ask John for the amount of the bill.
// let bill = +prompt("John, What is the bill amount?")
// Create the program explained above.
// In the end, John would like to know:
// Tip amount.
// Final bill (bill + tip).
// (NOTE: To calculate 20% of a value, simply multiply it with 20/100 = 0.2)

// function tipCal(bill) {
//     var tip = 0
//     if (bill < 50){
//         tip = bill * 0.2;
//     }else if (50 <= bill < 200){
//         tip = bill * 0.15;
//     }else {bill * 0.1 ;
//     }
//     console.log("your tip is "+ tip);
//     // console.log("the total bill incuding tip is " + $[tip+bill]
//     console.log(`Your total bill is ${bill+tip}.`);
//     return;
// }

// tipCal(bill);

// ***************************************************************************************
// Exercise 7 : Vacations Costs

// Let’s create functions that calculate your vacation’s costs:

// Define a function called hotel_cost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.


// function hotel_cost(){

//     do {var nights = +prompt("How many nights to stay?")}
//     while (nights <= 0 || isNaN(nights));
//     return (nights * 140);
// }


// Define a function called plane_ride_cost().
// It should ask the user for their destination.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$
// If the user doesn’t answer or if the answer is not a string, ask again.

// function plane_ride_cost(){

//     do {var destination = prompt("Where  to?").toLowerCase( )}
//     while (!isNaN(destination) || destination == "");
//          if (destination === "london"){
//                  return 'plane ride cost 183$' ;   
//          }else if (destination === "paris"){
//                   return 'plane ride cost 220$';    
//           } else {
//                return 'plane ride cost 300$';
//     }
// }
// plane_ride_cost()

// Define a function called rental_car_cost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental.


// function rental_car_cost() {

//     do {
//         var rentDay = +prompt("How many days to to rent a car?");
//     }
//     while (rentDay <= 0 || isNaN(rentDay));
//     if (rentDay > 10) {
//         return (rentDay * 40 * 0.95);
//     } else {
//         return (rentDay * 40);
//     }
// }
// rental_car_cost()

// Define a function called total_vacation_cost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotel_cost(plane_ride_cost(
// Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the total_vacation_cost() function.

