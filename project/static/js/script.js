$(document).ready(function() {
  $('#add-field-button').click(function() {
    var clonedField = $('#fields input:last').clone();
    clonedField.attr('name', 'field' + ($('#fields input').length + 1));
    $('#fields').append(clonedField);
    $('#fields').append("<br>");
  });
});