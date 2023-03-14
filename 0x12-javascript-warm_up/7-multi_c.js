#!/usr/bin/node
if (!process.argv[2]) {
  console.log('Missing number of occurrences');
} else {
  let i = parseInt(process.argv[2]);
  for (; i > 0; i--) {
    console.log('C is fun');
  }
}
