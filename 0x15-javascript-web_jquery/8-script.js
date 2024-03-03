$(function(){
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data, status){
    data.each(function(index, film){
      $('UL#list_movies').append('<li></li>').text(film.title);
    });
  });
});
