#!/usr/bin/node

const arg = parseInt(process.argv[2]);

if (arg) {
  for (let i = 0; i < arg; i++) {
    let x = '';
    for (let j = 0; j < arg; j++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
