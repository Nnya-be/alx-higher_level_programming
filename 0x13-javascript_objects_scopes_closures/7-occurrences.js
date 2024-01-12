#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, item) => {
    return (item === searchElement) ? count + 1 : count;
  }, 0);
};
