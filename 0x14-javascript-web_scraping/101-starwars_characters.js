#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

function fetchCharacterDetails (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

async function printCharacterNames (characters) {
  try {
    const characterNames = await Promise.all(characters.map(fetchCharacterDetails));
    characterNames.forEach(name => console.log(name));
  } catch (error) {
    console.error(error);
  }
}

request(`${apiUrl}${movieId}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    printCharacterNames(characters);
  }
});
