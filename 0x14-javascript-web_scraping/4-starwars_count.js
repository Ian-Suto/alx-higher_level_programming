#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  let data = JSON.parse(body).results;
  data = data.filter(({ characters }) => characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
  console.log(data.length);
})
;
