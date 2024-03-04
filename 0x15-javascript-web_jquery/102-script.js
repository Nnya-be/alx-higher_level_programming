$(function() {
  $('#btn_translate').on('click', function() {
    var languageCode = $('#language_code').val();
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/',
      type: 'GET',
      data: { lang: languageCode },
      success: function(response) {
        $('#hello').text(response.hello);
      },
      error: function() {
        $('#hello').text('Translation not available for the specified language.');
      }
    });
  });
});
