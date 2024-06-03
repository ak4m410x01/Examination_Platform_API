$(document).ready(function () {
  // on updating data
  $('#update').click(function () {
    $('input').each(function (el) {
      $(this).removeAttr('readonly');
      // console.log("abeer");
    });
    $(this).css('background-color', 'white'); // Change the button color to green
  });

  // on saving data
  $('#save').click(function () {
    $('input').each(function (el) {
      $(this).attr('readonly', 'true');
      // console.log("abeer");
    });
    $('#update').css('background-color', '#b3d6f5'); // Change the button color to green
  })
  ;
});
