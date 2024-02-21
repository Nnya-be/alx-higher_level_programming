#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

function countMoviesWithCharacter (apiUrl, characterId) {
  return new Promise((resolve, reject) => {
    request(apiUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode === 200) {
        const movies = JSON.parse(body).results;
        const count = movies.reduce((acc, movie) => {
          const characters = movie.characters.map(character => character.split('/').slice(-2, -1)[0]);
          if (characters.includes(characterId)) {
            return acc + 1;
          }
          return acc;
        }, 0);
        resolve(count);
      } else {
        reject(new Error('Invalid API response'));
      }
    });
  });
}

const characterId = '18';

countMoviesWithCharacter(apiUrl, characterId)
  .then(count => console.log(count))
  .catch(error => console.error(error));
