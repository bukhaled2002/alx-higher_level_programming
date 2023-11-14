#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let temp = [];
    for (let i = 0; i < this.height; i++) {
      temp[i] = [];
      for (let j = 0; j < this.width; j++) {
        temp[i].push('X');
      }
      temp[i] = temp[i].join('');
    }
    temp = temp.join('\n');
    console.log(temp);
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
