#!/usr/bin/node
const { dict } = require('./101-data');

const computeUsersByOccurrence = (originalDict) => {
  const usersByOccurrence = {};

  for (const userId in originalDict) {
    const occurrences = originalDict[userId];

    if (!usersByOccurrence[occurrences]) {
      usersByOccurrence[occurrences] = [];
    }

    usersByOccurrence[occurrences].push(userId);
  }

  return usersByOccurrence;
};
const result = computeUsersByOccurrence(dict);

console.log(result);
