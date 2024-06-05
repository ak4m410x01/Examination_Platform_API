$(document).ready(function () {
  $('form').on('submit', function (event) {
    // Prevent the form from submitting the traditional way
    event.preventDefault();
    $('#flash-message').text('Incorrect username or password.').hide();

    const username = $('#username').val();
    const password = $('#pass').val();

    $.ajax({
      url: 'http://localhost/api/auth/token/',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({
        username: username,
        password: password
      }),
      success: function () {
        window.location.href = 'http://localhost/dashboard';
      },
      error: function () {
        $('#flash-message').text('Incorrect username or password.').show();
      }
    });
  });
});
