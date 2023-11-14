#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
  consloe.log(`${count}: ${item}`);
  count++;
};
