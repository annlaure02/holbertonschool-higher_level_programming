#!/usr/bin/node

const sentence = 'C is fun';
const x = parseInt(process.argv[2]);

if (x) {
  for (let i = 0; i < x; i++) {
    console.log(sentence);
  }
} else {
  console.log('Missing number of occurrences');
}
