

function ControladorTab(event, id){
  var i, x, tablinks;
  event.preventDefault();
  x = document.getElementsByClassName("city");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" w3-border-black", "");
  }

  entradas = document.getElementsByClassName("entrada");
  for (i = 0; i < entradas.length; i++) {
    entradas[i].style.display = "none";
  }

  switch(id){
    case "protocolo":
        AgregarPreguntas();
        document.getElementById("div_preguntas").style.display = "block";
        break;
    case "Formulario":
        AgregarPreguntas();
        AgregarProtocoloDeBusqueda();
        AgregarCriterios();
        document.getElementById("div_preguntas").style.display = "block";
        document.getElementById("div_criterios_calidad").style.display = "block";
        break;
    case "Criterios":
        AgregarPreguntas();
        AgregarProtocoloDeBusqueda();
        document.getElementById("div_protocolo_busqueda").style.display = "block";
        break;
    case "Validacion":
        AgregarPreguntas();
        AgregarCriterios();
        AgregarProtocoloDeBusqueda();
        document.getElementById("div_preguntas").style.display = "block";
        document.getElementById("div_protocolo_busqueda").style.display = "block";
        document.getElementById("div_criterios_seleccion").style.display = "block";
        document.getElementById("div_criterios_calidad").style.display = "block";
        break;
  }

  document.getElementById(id).style.display = "block";
  event.currentTarget.className += " w3-border-black";

}
document.getElementById("esp_preg").click();
function AgregarProtocoloDeBusqueda(){

  while (document.getElementById("insertar_cadena").firstChild){
    document.getElementById("insertar_cadena").removeChild(document.getElementById("insertar_cadena").firstChild);
  }
  while (document.getElementById("insertar_metadatos").firstChild){
    document.getElementById("insertar_metadatos").removeChild(document.getElementById("insertar_metadatos").firstChild);
  }
  while (document.getElementById("insertar_bibliotecas").firstChild){
    document.getElementById("insertar_bibliotecas").removeChild(document.getElementById("insertar_bibliotecas").firstChild);
  }

  if(document.getElementById("id_cadena_de_busqueda").value != ""){
    var node = document.createElement("p");
    var textnode = document.createTextNode(document.getElementById("id_cadena_de_busqueda").value);
    node.appendChild(textnode);
    node.className = "w3-margin-left" ;                               
    document.getElementById("insertar_cadena").appendChild(node);
  }

  select_metadatos = document.getElementById("id_metadatos");
  haymetadato = false;
  for(i=0;i< select_metadatos.options.length; i++){
    if (select_metadatos.options[i].selected){
      var node = document.createElement("LI");              
      var textnode = document.createTextNode(select_metadatos.options[i].text);   
      node.appendChild(textnode);                              
      document.getElementById("insertar_metadatos").appendChild(node);
      haymetadato = true;
    }
  }

  select_bibliotecas = document.getElementById("id_bibliotecas");
  var haybiblioteca = false;
  for(i=0;i< select_bibliotecas.options.length; i++){
    if (select_bibliotecas.options[i].selected){
      var node = document.createElement("LI");              
      var textnode = document.createTextNode(select_bibliotecas.options[i].text);   
      node.appendChild(textnode);                              
      document.getElementById("insertar_bibliotecas").appendChild(node);
      var haybiblioteca = true
    }
  }
  
  if ((document.getElementById("id_cadena_de_busqueda").value == "") || !haybiblioteca || !haymetadato){
    document.getElementById("notificacion-protocolo").style.display = "block";
    document.getElementById("div_proto").classList.remove("w3-border-green", "w3-border-red");
    document.getElementById("div_proto").className += " w3-border-red";
  }
  else{
    document.getElementById("notificacion-protocolo").style.display = "none";
    document.getElementById("div_proto").classList.remove("w3-border-red", "w3-border-green");
    document.getElementById("div_proto").className += " w3-border-green";
  }
}

function AgregarPreguntas(){
   cant_preguntas = document.getElementById("nuevas_preguntas").childElementCount;
    var str = "pregunta-";

    while (document.getElementById("lista_preguntas").firstChild) {
      document.getElementById("lista_preguntas").removeChild(document.getElementById("lista_preguntas").firstChild);
    }

    if( document.getElementById(str.concat("0")).value != "" || cant_preguntas > 0){
      for (i =1; i <= cant_preguntas; i++){
        if(document.getElementById(str.concat(i)).value != "BORRAR" && document.getElementById(str.concat(i)).value != "" ){
          var node = document.createElement("LI");              
          var textnode = document.createTextNode(document.getElementById(str.concat(i)).value);   
          node.appendChild(textnode);                              
          document.getElementById("lista_preguntas").appendChild(node); 
        }
      }
      if( document.getElementById(str.concat("0")).value != ""){
      var node = document.createElement("LI");              
      var textnode = document.createTextNode(document.getElementById(str.concat("0")).value);   
      node.appendChild(textnode);                              
      document.getElementById("lista_preguntas").appendChild(node);
      }
      document.getElementById("notificacion-preguntas").style.display = "none";
      document.getElementById("esp_preg").classList.remove("w3-border-red", "w3-border-green");
      document.getElementById("esp_preg").className += " w3-border-green";
    }
    else{
      document.getElementById("notificacion-preguntas").style.display = "block";
      document.getElementById("esp_preg").classList.remove("w3-border-green", "w3-border-red");
      document.getElementById("esp_preg").className += " w3-border-red";
    }
}

function AgregarCriterios(){
  var tabla = document.getElementById("tabla_criterios");
  while (document.getElementById("lista_criterios_calidad").firstChild) {
    document.getElementById("lista_criterios_calidad").removeChild(document.getElementById("lista_criterios_calidad").firstChild);
  }
  while (document.getElementById("lista_criterios_inclusion").firstChild) {
    document.getElementById("lista_criterios_inclusion").removeChild(document.getElementById("lista_criterios_inclusion").firstChild);
  }
  while (document.getElementById("lista_criterios_exclusion").firstChild) {
    document.getElementById("lista_criterios_exclusion").removeChild(document.getElementById("lista_criterios_exclusion").firstChild);
  }
  if(tabla.rows.length == 1){
    document.getElementById("notificacion-criterios").style.display = "block";
    document.getElementById("div_cri").classList.remove("w3-border-green", "w3-border-red");
    document.getElementById("div_cri").className += " w3-border-red";
  }else{
    for(i=1; i<tabla.rows.length; i++){
      if( tabla.rows[i].cells[0].innerHTML !="BORRAR"){

        var node = document.createElement("LI");              
        var textnode = document.createTextNode(tabla.rows[i].cells[0].innerHTML);   
        node.appendChild(textnode);
        if(tabla.rows[i].cells[1].innerHTML == "CA"){
          document.getElementById("lista_criterios_calidad").appendChild(node);
        }else{
          if(tabla.rows[i].cells[1].innerHTML == "EX"){
            document.getElementById("lista_criterios_exclusion").appendChild(node);
          }else{
            document.getElementById("lista_criterios_inclusion").appendChild(node);
          }
        }
      }
    }
    document.getElementById("notificacion-criterios").style.display = "none";
    document.getElementById("div_cri").classList.remove("w3-border-red", "w3-border-green");
    document.getElementById("div_cri").className += " w3-border-green";
  }
}

function extraerCampos(){
  var campos = new FormData();
  var tabla = document.getElementById("tabla_campos_form");
  for(i=1; i<tabla.rows.length; i++){
    campos.append("campo-"+i,tabla.rows[i].cells[0].innerHTML);
  }
  campos.append("cant-campos", document.getElementById("id_campos_form-TOTAL_FORMS").value);
  return campos;
}

function nuevaPregunta(e){
  e.preventDefault();
  var form_idx = $('#id_preguntas-TOTAL_FORMS').val();

  $('#nuevas_preguntas').append($('#empty_form').html().replace(/__prefix__/g, form_idx));

  $('#pregunta-'+form_idx+'').val($('#pregunta-0').val());
  $('#pregunta-0').val("");

  $('#id_preguntas-TOTAL_FORMS').val(parseInt(form_idx) + 1);
  
};

function borrarPregunta(e){
  e.currentTarget.parentElement.parentElement.firstElementChild.firstElementChild.value = "BORRAR";
  e.currentTarget.parentElement.parentElement.style.display = 'none'; 
}

$(document).ready(function (){

 

 $('#insertar_criterio').click(function(e){

    var form_idx = $('#id_criterios-TOTAL_FORMS').val();
    e.preventDefault();
    if($('#id_criterio-__prefix__-descripcion').val($('#id_criterio-__prefix__-descripcion').val()) != "" ){

      $('<input>').attr('type','hidden').attr('id','id_criterio-'+form_idx+'-descripcion').attr('name','id_criterio-'+form_idx+'-descripcion').val($('#id_criterio-__prefix__-descripcion').val()).appendTo('#nuevos_criterios');
      $('<input>').attr('type','hidden').attr('id','id_criterio-'+form_idx+'-tipo').attr('name','id_criterio-'+form_idx+'-tipo').val($('#id_criterio-__prefix__-tipo').val()).appendTo('#nuevos_criterios');
      
      var nuevo_criterio = '<td>'+$('#id_criterio-__prefix__-descripcion').val()+"</td>";
      nuevo_criterio += '<td>'+$('#id_criterio-__prefix__-tipo').val()+"</td>";
      nuevo_criterio +='<td id="id_criterio-'+form_idx+'-"><i class="fa fa-remove borrar-linea"></i></td>';
      var tr = $('<tr></tr>').append(nuevo_criterio);

      $('#id_criterio-__prefix__-descripcion').val("");
      $('#id_criterios-TOTAL_FORMS').val(parseInt(form_idx) + 1);
      $('#tabla_criterios').append(tr);
    }
 });

 $('#insertar_campo').click(function(e){

  e.preventDefault();
  var form_idx = $('#id_campos_form-TOTAL_FORMS').val();
 
  var campo = '<input type="hidden" name="campos_form-'+form_idx+'-id" id="id_campos_form-'+form_idx+'-id" value="'+$('#id_campo_form-__prefix__-descripcion').val()+'">';
  
  $('#nuevos_campos_form').append(campo);

  var nuevo_campo = '<td>'+$('#id_campo_form-__prefix__-descripcion').val()+"</td>";
  nuevo_campo +='<td id="id_criterio-'+form_idx+'-"><i class="fa fa-remove borrar-linea"></i></td>';
  var tr = $('<tr class="w3-border-top"></tr>').append(nuevo_campo);

  $('#id_campo_form-__prefix__-descripcion').val("");
  $('#id_campos_form-TOTAL_FORMS').val(parseInt(form_idx) + 1);
  $('#tabla_campos_form').append(tr);
});

 $(document).on('click', '.borrar-linea', function(e) {
    e.preventDefault();
    //$('#'+$(this).parent().attr('id')+'div').hide();
     

    //var form_idx = $('#id_criterios-TOTAL_FORMS').val();
    //$('#id_criterios-TOTAL_FORMS').val(parseInt(form_idx) - 1);
    $(this).parent().parent().hide();
    $(this).parent().parent().children().first().text("BORRAR");
    
    if($('#'+$(this).parent().attr('id')+'descripcion').length){
      $('#'+$(this).parent().attr('id')+'descripcion').attr('value', 'BORRAR')
    }
    
});

$('#generar_formulario').click(function(e){
  e.preventDefault();
  var id_revision = $('#id_revision').val();
  datos = extraerCampos();
  $.ajax({
    url: '/crear_formulario/'+id_revision+'/',
    type : "POST",
    data: datos,
    processData: false,  // tell jQuery not to process the data
    contentType: false,   // tell jQuery not to set contentType
  });

  $('#notificacion-formulario').css({ display: "block" });
  $('#div_val').removeAttr("disabled");

})

});