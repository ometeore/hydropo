function disable_inputs(id) { 

    var checkBox = document.getElementById("manual_mode_" + id);
    var elmts = document.getElementsByClassName('disable_input_block_' + id);
    console.log(elmts + elmts.length)
    var inputs = document.getElementsByClassName('disable_input_' +id);

    // If the checkbox is checked, display the output text
    if (checkBox.checked == true){
        for(var i=0;i<elmts.length;i++)
        {
            elmts[i].style.display='flex';
        }
    } else {
        for(var i=0;i<elmts.length;i++)
        {
            elmts[i].style.display='none';
        }
        for(var i=0;i<inputs.length;i++)
        {
            inputs[i].checked=false;
        }
    }
}

function first_hide(){
    var elmts = document.getElementsByClassName('hide');
    var quer = window.location.search;
    console.log(quer);
    parameters = new URLSearchParams(quer);
    if(parameters.has('manual')){
        var checkBox_true = document.getElementById(parameters.get('tool'));
        checkBox_true.checked = true;
        id = checkBox_true.className.substr(14);
        checkBox_manual = document.getElementById("manual_mode_" + id);
        checkBox_manual.checked = true;
    }
    else{
        for(var i=0;i<elmts.length;i++)
        {
            elmts[i].style.display='none';
        }
    }
}

/*fait disparaitre les inputs au chargement de la page*/

first_hide();


function recupId(id) {
    var checkBox_true = document.getElementById(id);
    var checkBox_false = document.getElementsByClassName(checkBox_true.className);
    for(i=0; i<checkBox_false.length; i++){
        checkBox_false[i].checked = false;
    }
    checkBox_true.checked = true;

    var url_to_send = '/rpi/gestion?manual=on&tool=' + id;
    window.location.href = url_to_send;
}
