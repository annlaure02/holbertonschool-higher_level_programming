#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request.get('https://swapi-api.hbtn.io/api/films/' + id, function (error, response, body) {
  if (!error) {
    const films = JSON.parse(body);
    console.log(films.title);
  }
});
