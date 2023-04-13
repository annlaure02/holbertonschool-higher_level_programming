#!/usr/bin/node

const args = process.argv.slice(2).map(function (str) { return parseInt(str); });
const numbersSorted = args.sort((a, b) => a - b);
const lastsNumbers = numbersSorted.slice(-2);

if (process.argv.length <= 3) {
  console.log('0');
} else {
  console.log(lastsNumbers[0]);
}
