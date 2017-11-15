// Directions:
// Call the emotions() function so that it prints the output you see below, but instead of passing the laugh() function as an argument, pass an inline function expression instead.
//
// emotions("happy", laugh(2)); // you can use your laugh function from the previous quizzes
// Prints: "I am happy, haha!"
//
//

/*
 * Programming Quiz: Inline Functions (5-6)
 */

// don't change this code
// function emotions(myString, myFunc) {
//     console.log("I am " + myString + ", " + myFunc(2));
// }
//
// emotions(function mood(happy){
//   console.log("happy");
// },"ha");
//
// your code goes here
// call the emotions function here and pass in an
// inline function expression


// function declaration that takes in two arguments: a function for displaying
// a message, along with a name of a movie
function movies(messageFunction, name) {
  messageFunction(name);
}

// call the movies function, pass in the function and name of movie
movies(function displayFavorite(movieName) {
  console.log("My favorite movie is " + movieName);
}, "Finding Nemo");
