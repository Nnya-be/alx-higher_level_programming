#!/usr/bin/node

const request = require('request');
const endpoint = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];
const url = `${endpoint}${movieId}`;
const characterUrls = [];
const characterNames = [];
let count = 0;

function printCharacterNames () {
  for (let x = 0; x < characterNames.length; x++) {
    console.log(characterNames[x]);
  }
}

function fetchCharacterDetails (characterUrl) {
  request(characterUrl, function (error, response, body) {
    if (error) {
      return console.log(error);
    }

    characterNames.push(JSON.parse(body).name);
    count++;

    if (count === characterUrls.length) {
      printCharacterNames();
    }
  });
}

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }

  const characters = JSON.parse(body).characters;

  for (let m = 0; m < characters.length; m++) {
    characterUrls.push(characters[m]);
    fetchCharacterDetails(characters[m]);
  }
});
