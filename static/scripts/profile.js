$(document).ready(function () {
  // on updating data
  $('#update').click(function () {
    $('input').each(function (el) {
      $(this).removeAttr('readonly');
      // console.log("abeer");
    });
    $('select').each(function (el) {
      $(this).prop('disabled', false);
    });
    $(this).css('background-color', 'white'); // Change the button color to green
  });

  // on saving data
  $('#save').click(function () {
    $('input').each(function (el) {
      $(this).attr('readonly', 'true');
      // console.log("abeer");
    });
    $('select').each(function (el) {
      $(this).prop('disabled', true);
    });
    $('#update').css('background-color', '#b3d6f5'); // Change the button color to green
  });

  // Extract JWT token from cookie
  const token = document.cookie.replace(/(?:(?:^|.*;\s*)jwt\s*=\s*([^;]*).*$)|^.*$/, '$1');

  // Decode JWT token to get USER_ID
  const base64Url = token.split('.')[1];
  const base64 = base64Url.replace('-', '+').replace('_', '/');
  const jsonPayload = decodeURIComponent(atob(base64).split('').map(function (c) {
    return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
  }).join(''));

  function getURL (userRole) {
    const baseURL = 'http://127.0.0.1/api/accounts/';
    let url;

    switch (userRole) {
      case 'admin':
        url = baseURL + 'admins/';
        break;
      case 'instructor':
        url = baseURL + 'instructors/';
        break;
      case 'student':
        url = baseURL + 'students/';
        break;
      default:
        url = baseURL; // default URL if no role matches
    }

    return url;
  }

  const userId = JSON.parse(jsonPayload).user_id;
  const userRole = JSON.parse(jsonPayload).user_role;
  const url = getURL(userRole);

  // Fetch data from API endpoint
  $.ajax({
    url: url + userId + '/',
    type: 'GET',
    headers: {
      Authorization: 'Bearer ' + token
    },
    success: function (data) {
      // Insert data into HTML page
      $('#userName').val(data.username);
      $('.profile p').text(data.username);
      $('.mainData h3').text(data.username);

      $('#userEmail').val(data.email);
      $('#city').val(data.city);
      $('#level').val(data.level);
      $('#h-level').text('Level ' + data.level);
      $('#name1').val(data.first_name);
      $('#name2').val(data.second_name);
      $('#name3').val(data.third_name);
      $('#name4').val(data.fourth_name);
      $('#gender').val(data.gender);
      $('#birth_date').val(data.birth_date);
      $('#address').val(data.address);
      $('#phone_number').val(data.phone);
      $('#department').val(data.department.title);
      $('#specialization').val(data.courses[0].title);
      $('#joined_at').text('Joined at : ' + new Date(data.date_joined).toLocaleDateString());
    },
    error: function (jqXHR, textStatus, errorThrown) {
      // Insert error message into HTML page
      $('#flash-message').text(jqXHR.responseText || textStatus);
      $('#flash-message').show();
    }
  });
});
