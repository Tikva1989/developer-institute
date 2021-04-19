//part 1

function playTheGame() {

    var randomNum = Math.floor(Math.random() * 11);
    console.log(randomNum);
    var guess;
    var res = confirm("Would you like to play the game?");
    if (res == false) {
        alert("No problem, Goodbye.");
    } else {
        guess = +prompt("enter a number between 0 and 10:");
        if (guess == "") {
            alert("Sorry Not a number, Goodbye");
        } else if (guess > 10) {
            alert("Sorry it’s not a good number, Goodbye.");
        } else
            alert("Sorry Not a number, Goodbye");
    }
}

// //part 2

function test (userNumber,computerNumber){
    var userNumber = guess;
    var computerNumber = randomNum;
    if (userNumber == computerNumber ){
        alert("WINNER")

    }else if (userNumber > computerNumber){
        prompt("Your number is bigger then the computer’s, guess again");
    }else if ( userNumber < computerNumber){
        prompt(" Your number is smaller then the computer’s, guess again");
    }else if (guess > 3){
        alert ( "out of chances");
    }
    
}