#!/usr/bin/node
const i = parseInt(process.argv[2]);
if (isNaN(i) === true) {
  console.log('Missing size');
} else {
  for (let k = 0; k < i; k++) {
    let row = '';
    for (let j = 0; j < i; j++) row += 'X';
    console.log(row);
  }
}
