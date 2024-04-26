#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;
request(url, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
    } else if (response.statusCode !== 200) {
        console.error('Status:', response.statusCode);
    } else {
        const data = JSON.parse(body);
        const characters = data.characters;
        characters.forEach(characterUrl => {
            request(characterUrl, (error, response, body) => {
                if (error) {
                    console.error('Error:', error);
                } else if (response.statusCode !== 200) {
                    console.error('Status:', response.statusCode);
                } else {
                    const characterData = JSON.parse(body);
                    console.log(characterData.name);
                }
            });
        });
    }
});
