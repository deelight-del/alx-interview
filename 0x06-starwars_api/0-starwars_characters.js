#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

// Define function that will await.
async function printCharacters (characterUrl) {
  await request(characterUrl, (err, resp, body) => {
    if (err) { return; }
    console.log(JSON.parse(body).name);
  });
}

async function main () {
  request.get(url, function (err, resp, body) {
    if (err) {
      return;
    }
    JSON.parse(body).characters.forEach(
      async function (character) {
        await printCharacters(character);
      });
  });
}

main();
