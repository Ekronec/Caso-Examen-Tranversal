$(document).ready(function () {
    $.ajax({
        url: "https://apis.digital.gob.cl/dpa/regiones",
        type: "GET",
        crossDomain: true,
        dataType: "jsonp",
        success: function (data) {
          $.each(data, function (i, item) {
            $("#region").append(
              "<option value='" + item.codigo + "'>" + item.nombre + "</option>"
            );
          });
        },
        error: function (xhr, status, error) {
          console.log("Error al obtener las regiones: " + error);
        },
      });

});