/***********************************************************************
Write a function `countScores(people)` that takes in an array of score
objects (people) as its input. A score object has two key-value pairs:
a name (string) and a score (number). `countScores(people)` should
return an object that has key-value pairs where each name is a key and
the value is their total score.

Example 1

const ppl = [ 
    {name: "Pete", score: 10},
    {name: "Mike", score : 10},
    {name: "Pete", score: -8},
    {name: "Dexter", score: 12}
];

const countPpl = countScores(ppl);
countPpl; //=> { Pete: 2, Mike: 10, Dexter: 12 }

Example 2

const peeps = [
  {name: "Pete", score: 2},
  {name: "Dexter", score: 2},
  {name: "Mike", score: 2},
  {name: "Dexter", score: 2},
  {name: "Mike", score: 2},
  {name: "Pete", score: 2},
  {name: "Dexter", score: 2}
];
countScores(peeps); //=> { Pete: 4, Mike: 4, Dexter: 6 }
***********************************************************************/

function countScores(people) { // Establishing the function with an object input
  let finalScore = {}; // Create an object for the function to use
  for (let thing in people) { // For loop to iterate through all the keys in the object
    if (finalScore[people[thing].name]) { // Within each specific name
      finalScore[people[thing].name] = finalScore[people[thing].name] + people[thing].score; // Add the score from each name to those with the same name
    } else { // Else
      finalScore[people[thing].name] = people[thing].score; // Keep the same score if there is nothing to add
    } // Curly bracket to close else statement
  } // Curly bracket to close the for loop
  return finalScore; // Return the object
} // Curly bracket to close the function