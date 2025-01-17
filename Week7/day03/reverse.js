'use strict';
// - Create a variable named `aj`
//   with the following content: `[3, 4, 5, 6, 7]`
// - Reverse the order of the elements in `aj`
// 		- do it with the built in method
//		- do it with creating a new temp array and a loop
// - Print the elements of the reversed `aj`

var aj = [3, 4, 5, 6, 7];

//with builtin method
aj = aj.reverse();
console.log(aj);

//temp array and loop
var aj = [3, 4, 5, 6, 7];
var ajReversed = [];
for (var item = aj.length; item > 0; item--) {
    var elementBackwards = aj.shift();
    ajReversed.unshift(elementBackwards);
}

console.log(ajReversed);
