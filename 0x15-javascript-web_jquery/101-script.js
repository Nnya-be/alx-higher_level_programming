$(function(){
  $('#add_item').on('click', function(){
    $('<li>Item</li>').appendTo('.my_list');
  });

  $('#remove_item').on('click', function(){
    $('.my_list li:last-child').remove();
  });

  $('#clear_list').on('click', function(){
    $('.my_list').empty();
  });
});
