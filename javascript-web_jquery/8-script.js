#!/usr/bin/node

$(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(url, function (data) {
    $.each(data.results, function (index, value) {
      $('UL#list_movies').append('<li>' + value.title + '</li>');
    });
  });
});
