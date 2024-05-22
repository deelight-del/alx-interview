#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

// Define function that will convert the return a
// promise.
function makeUrlPromise (characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (err, resp, body) => {
      if (err) { reject(err); }
      resolve(JSON.parse(body).name);
    });
  });
}

function main () {
  request.get(url, (err, resp, body) => {
    if (err) { return; }
    const charactersUrl = JSON.parse(body).characters;
    const urlPromisedNames = charactersUrl.map((name) => makeUrlPromise(name));
    Promise.all(urlPromisedNames).then((names) => {
      for (const name_ of names) {
        console.log(name_);
      }
    });
  });
}

main();
