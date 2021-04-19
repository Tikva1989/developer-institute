var sentence = "The movie is not that bad I like it.";
// var sentence = "The movie is bad that not I like it.";

//2. Create a variable called wordNot where it’s value is the 
//first appearance of the substring “not” (from the sentence variable).

let sentenceArray = sentence.split(" ");

let wordNot = sentenceArray.indexOf("not");
let wordBad = sentenceArray.indexOf("bad");

if (wordBad > wordNot){
    sentenceArray.splice(wordNot, (wordBad-wordNot+1), "good");
    let result = sentenceArray.join(" ");
    console.log(result);
}else { 
    let result = sentenceArray.join(" ");
    console.log(result);
    
}