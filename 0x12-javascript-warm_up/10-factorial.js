#!/usr/bin/node
function factorial (number) {
  if (number === 1 || number === 0) { return (1); } else if (isNaN(number)) { return (1); } else { return (number * factorial(number - 1)); }
}

const number = parseInt(process.argv[2]);
console.log(factorial(number));
