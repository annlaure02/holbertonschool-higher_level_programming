#!/usr/bin/node

function factorial (x) {
  if (x > 0) {
    return x * factorial(x - 1);
  } else {
    return 1;
  }
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));
