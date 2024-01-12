#!/usr/bin/node
class Square extends require('./5-square.js')
{
  constructor(size) {
    super(size);
  }

  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    
    for (let i = 0; i < this.size; i++) {
      console.log("h");
    }
  }
}
module.exports = Square;
