#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const items = list.filter(item => item === searchElement);
  return items.length;
};
