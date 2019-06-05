

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
