
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