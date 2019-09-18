// Get the Sidebar
var mySidebar = document.getElementById("mySidebar");

// Get the DIV with overlay effect
var overlayBg = document.getElementById("myOverlay");

// Toggle between showing and hiding the sidebar, and add overlay effect
function w3_open() {
  if (mySidebar.style.display === 'block') {
    mySidebar.style.display = 'none';
    overlayBg.style.display = "none";
  } else {
    mySidebar.style.display = 'block';
    overlayBg.style.display = "block";
  }
}

// Close the sidebar with the close button
function w3_close() {
  mySidebar.style.display = "none";
  overlayBg.style.display = "none";
}

// add clases for inputs
function AgregarClase() {
    
  var inputs = document.querySelectorAll('input');

  var i;

  for(i = 0; i< inputs.length ; i++){
      if(inputs[i].type == 'checkbox'){
          inputs[i].classList.add("w3-radio")
      }else{
          inputs[i].classList.add("w3-input")
          inputs[i].classList.add("w3-border")
          inputs[i].classList.add("w3-round")
      }
  }

  var selects = document.querySelectorAll('select');
   for(i = 0; i< selects.length ; i++){
      selects[i].classList.add("w3-select")
      selects[i].classList.add("w3-border")
  }

  var selects = document.querySelectorAll('select');
   for(i = 0; i< selects.length ; i++){
      selects[i].classList.add("w3-select")
      selects[i].classList.add("w3-border")
  }
}