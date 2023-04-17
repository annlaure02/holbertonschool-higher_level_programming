#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (err, response) {
  console.error(err);
  console.log('code:', response.statusCode);
});
