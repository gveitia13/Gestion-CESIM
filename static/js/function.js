$(document).ready(function () {
  $('.select2').select2({
    placeholder: 'Seleccionar proyectos(s)'
  });
});

//Auxiliary method: submit with ajax and jQuery
function ajaxFunction(url, parameters, type, callback, async = true) {
  $.ajax({
    url: url,
    type: type,
    data: parameters,
    dataType: 'json',
    processData: false,
    contentType: false,
    async: async
  })
    .done(function (data) {
      // callback(data)
      if (!data.hasOwnProperty('error')) {
        callback(data)
        return false
      }
    })
    .fail(function (jqXHR, textStatus, errorThrown) {
      alert(textStatus + ': ' + errorThrown)
    })
    .always(function (data) {
    })
}

//For Delete using jQuery confirm plugin and Jquery with ajax
let submit_with_ajax_alert = function (url, title, content, parameters, callback, icon) {
  $.confirm({
    theme: 'material',
    title: title,
    icon: icon,
    content: content,
    columnClass: 'small',
    typeAnimated: true,
    cancelButtonClass: 'bg-gradient-primary circular',
    draggable: true,
    dragWindowBorder: false,
    buttons: {
      info: {
        text: 'Si',
        btnClass: 'bg-gradient-primary circular',
        action: function () {
          ajaxFunction(url, parameters, 'POST', callback, true)
        }
      },
      danger: {
        text: 'No',
        btnClass: 'bg-gradient-danger circular',
        action: () => {
        }
      }
    }
  })
}