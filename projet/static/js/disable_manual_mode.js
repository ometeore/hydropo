function first_hide(){

    url = window.location.search;
    const urlParams = new URLSearchParams(url);
    var elmts = document.getElementsByClassName('hide');
    for(var i=0;i<elmts.length;i++)
    {
        elmts[i].style.display='none';
    }

    if(urlParams.has('manual')){
        name_elm = urlParams.get('name');
        console.log(name_elm)
        elmts = document.getElementsByClassName('disable_input_block_' + name_elm);
        for(var i=0;i<elmts.length;i++)
        {
            elmts[i].style.display='flex';
        }
        var checkBox = document.getElementById("manual_mode_" + name_elm);
        checkBox.checked = true;
        if(urlParams.has('tool')){
            var checkBox = document.getElementById(urlParams.get('tool')+ '_' + name_elm);
            checkBox.checked = true;
        }
    }
}

/*fait disparaitre les inputs au chargement de la page*/

first_hide();




function switch_manual_mode(id, name) { 
    console.log("manual_mode_" + id)
    console.log(name.id)
    var checkBox = document.getElementById("manual_mode_" + name.id);

    // If the checkbox is checked, display the output text
    if (checkBox.checked == true){
        var url_to_send = '/rpi/gestion?manual=True&name=' + name.id;
        window.location.href = url_to_send;
    }
    if(checkBox.checked == false) {
        var url_to_send = '/rpi/gestion';
        window.location.href = url_to_send;
    }
}




function recupId(id) {
    var checkBox_true = document.getElementById(id);
    var checkBox_false = document.getElementsByClassName(checkBox_true.className);
    for(i=0; i<checkBox_false.length; i++){
        checkBox_false[i].checked = false;
    }
    checkBox_true.checked = true;
    res = id.split('_')
    var url_to_send = '/rpi/gestion?manual=True&tool=' + res[0] + '&name=' + res[1];
    window.location.href = url_to_send;
}
