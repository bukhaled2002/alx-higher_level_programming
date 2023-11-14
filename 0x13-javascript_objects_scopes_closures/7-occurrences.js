#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  items = list.filter(item => item == searchElement);
  return items.length;
};
