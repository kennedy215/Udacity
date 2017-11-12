// Directions:
// Write a function called laugh() that takes one parameter, num that represents the number of "ha"s to return.
//
// TIP: You might need a loop to solve this!
// Here's an example of the output and how to call the function that you will write:

  function laugh(num) {
    var word = "";
    for(i = 0; i < num; i++) {
      word = word + "ha"
    }
    return word +"!";
  }

console.log(laugh(3));
