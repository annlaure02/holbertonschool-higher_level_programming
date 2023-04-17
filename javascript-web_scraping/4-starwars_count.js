#!/usr/bin/node

const request = require('request');
let count = 0;
const url = String(process.argv[2]);
const characterId = '18';

request({
  url: url,
  json: true
}, (err, response, body) => {
  if (err) {
    console.log('Error:', err);
  } else {
    for (const i in body.results) {
      for (const j of body.results[i].characters) {
        if (j === `https://swapi-api.hbtn.io/api/people/${characterId}/`) {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});
