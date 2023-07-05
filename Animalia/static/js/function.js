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
  
  $("#region").change(function () {
    var idRegion = $("#region").val();
    $("#provincia").attr("disabled",false);
    $("#provincia").empty();
    $("#provincia").append("<option hidden disable>Seleccione una opcion</option>");
    $("#comuna").empty();
    $("#comuna").append("<option hidden disable>Seleccione una opcion</option>");

    $.ajax({
      url: "https://apis.digital.gob.cl/dpa/regiones/"+idRegion+"/provincias",
      type: "GET",
      crossDomain: true,
      dataType: "jsonp",
      success: function (data) {
        $.each(data, function (i, item) {
          $("#provincia").append(
            "<option value='" + item.codigo + "'>" + item.nombre + "</option>"
          );
        });
      },
      error: function (xhr, status, error) {
        console.log("Error al obtener las regiones: " + error);
      },
    });
  });

  $("#provincia").change(function () {
    var idRegion = $("#region").val();
    var idProvincia = $("#provincia").val();
    $("#comuna").attr("disabled",false);
    $("#comuna").empty();
    $("#comuna").append("<option hidden disable>Seleccione una opcion</option>");
    $.ajax({
      url: "https://apis.digital.gob.cl/dpa/regiones/"+idRegion+"/provincias/"+idProvincia+"/comunas",
      type: "GET",
      crossDomain: true,
      dataType: "jsonp",
      success: function (data) {
        $.each(data, function (i, item) {
          $("#comuna").append(
            "<option value='" + item.codigo + "'>" + item.nombre + "</option>"
          );
        });
      },
      error: function (xhr, status, error) {
        console.log("Error al obtener las regiones: " + error);
      },
    });
  });
});