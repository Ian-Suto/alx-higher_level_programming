#!/usr/bin/node
function maxOfArray (array) {
  return Math.max.apply(Math, array);
}
if (!process.argv[2] || !process.argv[3]) {
  console.log('0');
} else {
  const array = process.argv.splice(2);
  const numberArray = array.map(Number);
  console.log(maxOfArray(numberArray));
}
