#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (s) {
    super(s, s);
  }

  charPrint (c) {
    if (!c) this.print();
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
