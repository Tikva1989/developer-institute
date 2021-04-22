var btn = document.getElementById("lib-button");


var libIt = function(){
    var storyDiv = document.getElementById("story");
    let noun = document.querySelector("#noun");
    let adjective = document.querySelector("#adjective");
    let person = document.querySelector("#person");
    let verb = document.querySelector("#verb");
    let place = document.querySelector("#place");
    let story = document.querySelector("#story");
    let button = document.querySelector("#lib-button");
    storyDiv.innerHTML = `some of  ${adjective.value} is to ${verb.value} while in ${place.value} some may ${noun.value} ${person.value}`;
};
btn.addEventListener("click", libIt);
