#!/usr/bin/node

/*
Imports a dict of occurrences by user id and computes a dict
 of user ids by occurrence
*/

const dict = require('./101-data.js').dict;
const newDict = {};
for (const key in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [key];
  } else {
    newDict[dict[key]].push(key);
  }
}
console.log(newDict);
