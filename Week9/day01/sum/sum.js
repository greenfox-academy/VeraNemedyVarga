// Sum
//
// Create a sum method in your class which has a list of integers as parameter
// It should return the sum of the elements in the list
// Follow these steps:
// Add a new test case
// Instantiate your class
// create a list of integers
// use the t.equal to test the result of the created sum method
// Run it
// Create different tests where you
// test your method with an empyt list
// with a list with one element in it
// with multiple elements in it
// with a null
// with a string
// Run them
// Fix your code if needed
'use strict'
 let sumClass = {
     sum: function (arr) {
         let summa = 0;
         if (Array.isArray(arr) === false) {
             throw new Error('parameter is not a list')
         } else {
             arr.forEach( function(el) {
                 summa += el;
             });
             return summa;
         }
     }
 }

console.log(sumClass.sum([1, 2, 3]));
module.exports = sumClass;
