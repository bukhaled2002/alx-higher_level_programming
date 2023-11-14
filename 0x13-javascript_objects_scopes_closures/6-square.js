#!/usr/bin/node
const Square = require('./5-square');

class Square extends Square {
  constructor (s) {
    super(s, s);
  }

  charPrint (c) {
    if (!c) super.print();
    else {
      let temp = [];
      for (let i = 0; i < this.height; i++) {
        temp[i] = [];
        for (let j = 0; j < this.width; j++) {
          temp[i].push(c);
        }
        temp[i] = temp[i].join('');
      }
      temp = temp.join('\n');
      console.log(temp);
    }
  }
}
module.exports = Square;
