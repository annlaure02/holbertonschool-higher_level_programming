#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;

request.get(url, function (error, response, body) {
  if (error) throw (error);
  const films = JSON.parse(body);
  for (let i = 0; i < films.results.length; i++) {
    const characters = films.results[i].characters;
    for (let j = 0; j < characters.length; j++) {
      const charID = characters[j].match('18');
      if (charID > 0) {
        count++;
      }
    }
  }
  console.log(count);
});
