

document.getElementById('MetaInformacion').style.display = "block";

function ControladorTab(evt, id) {
  var i, x, tablinks;
  x = document.getElementsByClassName("city");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < x.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" w3-border-black", "");
  }
  document.getElementById(id).style.display = "block";
  evt.currentTarget.firstElementChild.className += " w3-border-black";
}

$(document).ready(function () {

  $('#tabla_criterios').tablesorter(); 

  $('#add').click(function(e){
    e.preventDefault();

    var form_idx = $('#id_preguntas-TOTAL_FORMS').val();

    $('#nuevas_preguntas').append($('#empty_form').html().replace(/__prefix__/g, form_idx));

    $('#id_preguntas-'+form_idx+'-pregunta').val($('#id_preguntas-0-pregunta').val());
    $('#id_preguntas-0-pregunta').val("");

    $('#id_preguntas-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    
  });

  $(document).on('click', '.remove', function(e) {
    e.preventDefault();
      
    //var form_idx = $('#id_preguntas-TOTAL_FORMS').val();
    //$('#id_preguntas-TOTAL_FORMS').val(parseInt(form_idx) - 1);
    $(this).parent().parent().remove()
  });

 $('#insertar_criterio').click(function(e){

    e.preventDefault();
    var form_idx = $('#id_criterios-TOTAL_FORMS').val();
    $('#nuevos_criterios').append($('<div id="id_criterios-'+form_idx+'-div"></div>').append($('#criterio_empty_form').html().replace(/__prefix__/g, form_idx)));
    $('#id_criterios-'+form_idx+'-descripcion').val($('#id_criterios-0-descripcion').val());
    $('#id_criterios-'+form_idx+'-tipo').val($('#id_criterios-0-tipo').val());


    var nuevo_criterio = '<td>'+$('#id_criterios-0-descripcion').val()+"</td>";
    nuevo_criterio += '<td>'+$('#id_criterios-0-tipo').val()+"</td>"
    nuevo_criterio +='<td id="id_criterios-'+form_idx+'-"><i class="fa fa-remove borrar-linea"></i></td>'
    var tr = $('<tr></tr>').append(nuevo_criterio);
    
    $('#id_criterios-0-descripcion').val("");
    $('#id_criterios-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    $('#tabla_criterios').append(tr);
 })

 $(document).on('click', '.borrar-linea', function(e) {
  e.preventDefault();
  $('#'+$(this).parent().attr('id')+'div').remove();  
  //var form_idx = $('#id_criterios-TOTAL_FORMS').val();
  //$('#id_criterios-TOTAL_FORMS').val(parseInt(form_idx) - 1);
  $(this).parent().parent().remove()
  
});


  

});