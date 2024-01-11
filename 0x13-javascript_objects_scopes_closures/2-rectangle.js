#!/usr/bin/node
class Rectangle {
  constructor (w = 0, h = 0) {
    if (w < 1 || h < 1) { return this; }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
