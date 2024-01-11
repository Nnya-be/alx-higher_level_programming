#!/usr/bin/node
class Rectangle {
  constructor (w = 0, h = 0) {
    if (w < 1 || h < 1) { return this; }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let shape = '';
      for (let j = 0; j < this.width; j++) {
        shape += 'X';
      }
      console.log(shape);
    }
  }

  rotate () {
    const height = this.height;
    this.height = this.width;
    this.width = height;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
