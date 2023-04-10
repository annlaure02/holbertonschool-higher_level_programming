#!/usr/bin/node

const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let char = '';
      for (let j = 0; j < this.height; j++) {
        if (c === undefined) {
          char += 'X';
        } else {
          char += 'C';
        }
      }
      console.log(char)
    }
  }
}

module.exports = Square;
