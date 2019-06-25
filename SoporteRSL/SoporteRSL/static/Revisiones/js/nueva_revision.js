

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


  $('#add').click(function(e){
    e.preventDefault();

    var form_idx = $('#id_preguntas-TOTAL_FORMS').val();

    $('#nuevas_preguntas').append($('#empty_form').html().replace(/__prefix__/g, form_idx));

    $('#pregunta-'+form_idx+'').val($('#pregunta-0').val());
    $('#pregunta-0').val("");

    $('#id_preguntas-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    
  });

  $(document).on('click', '.remove', function(e) {
    e.preventDefault();
      
    $(this).parent().parent().find('input').val("BORRAR");
    //var form_idx = $('#id_preguntas-TOTAL_FORMS').val();
    //$('#id_preguntas-TOTAL_FORMS').val(parseInt(form_idx) - 1);
    $(this).parent().parent().hide()
  });

 $('#insertar_criterio').click(function(e){

    e.preventDefault();
    var form_idx = $('#id_criterios-TOTAL_FORMS').val();

    $('#nuevos_criterios').append($('<div id="id_criterio-'+form_idx+'-div" class="criterio"></div>').append($('#criterio_empty_form').html().replace(/__prefix__/g, form_idx)));
    $('#id_criterio-'+form_idx+'-descripcion').val($('#id_criterio-__prefix__-descripcion').val());
    $('#id_criterio-'+form_idx+'-tipo').val($('#id_criterio-__prefix__-tipo').val());
    
    
    
    
    var nuevo_criterio = '<td>'+$('#id_criterio-__prefix__-descripcion').val()+"</td>";
    nuevo_criterio += '<td>'+$('#id_criterio-__prefix__-tipo').val()+"</td>"
    nuevo_criterio +='<td id="id_criterio-'+form_idx+'-"><i class="fa fa-remove borrar-linea"></i></td>'
    var tr = $('<tr></tr>').append(nuevo_criterio);

    $('#id_criterio-__prefix__-descripcion').val("");
    $('#id_criterios-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    $('#tabla_criterios').append(tr);
 })

 $(document).on('click', '.borrar-linea', function(e) {
    e.preventDefault();

    //$('#'+$(this).parent().attr('id')+'div').hide();
    $('#'+$(this).parent().attr('id')+'descripcion').val("BORRAR"); 

    //var form_idx = $('#id_criterios-TOTAL_FORMS').val();
    //$('#id_criterios-TOTAL_FORMS').val(parseInt(form_idx) - 1);
    $(this).parent().parent().hide();
    
});


  

});