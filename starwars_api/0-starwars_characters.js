#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;
request(url, async (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    for (const characterUrl of characters) {
      await new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            console.log(JSON.parse(body).name);
            resolve();
          } else {
            console.error('Error:', error);
            reject();
          }
        });
      });
    }
  } else {
    console.error('Error:', error);
  }
});
