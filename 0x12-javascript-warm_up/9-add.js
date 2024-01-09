#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const number1 = parseInt(process.argv[2]);
const number2 = parseInt(process.argv[3]);
add(number1, number2);
