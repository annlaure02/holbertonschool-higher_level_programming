#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) throw (error);
  const todos = JSON.parse(body);
  const tasksCompleted = {};
  for (let i = 0; i < todos.length; i++) {
    if (todos[i].completed === true) {
      if (tasksCompleted[todos[i].userId]) {
        tasksCompleted[todos[i].userId]++;
      } else {
        tasksCompleted[todos[i].userId] = 1;
      }
    }
  }
  console.log(tasksCompleted);
});
