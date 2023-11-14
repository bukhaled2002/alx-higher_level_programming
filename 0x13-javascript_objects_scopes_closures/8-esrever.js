#!/usr/bin/node
exports.esrever = function (list){
  const items = []
  for(let i = 0; i < list.length; i++){
  items.push(list[list.length - 1 -i]);
  }
  return items;
};
