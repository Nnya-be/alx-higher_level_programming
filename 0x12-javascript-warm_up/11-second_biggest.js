#!/usr/bin/node
function secondLargest (numbers) {
  if (!numbers || numbers.length < 2) { return (0); }
  const unique = Array.from(new Set(numbers.map(Number)));
  const sorted = unique.sort((a, b) => b - a);
  return sorted[1];
}
const args = process.argv.slice(2);
console.log(secondLargest(args));
