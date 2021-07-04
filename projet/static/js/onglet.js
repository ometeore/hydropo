
function HideOnglet() {
    var onglets = document.getElementsByClassName("onglet");
    for (var i=0; i < onglets.length; i++){
        onglets.item(i).style.display = 'none';
    }
}
function ShowOnglet(id){
    HideOnglet()
    var onglet = document.getElementById("onglet_" + id);
    onglet.style.display = 'block';
}

function ShowFirst(){
    var onglets = document.getElementsByClassName("onglet");
    for (var i=0; i < onglets.length; i++){
        if(i == 0){
            onglets.item(i).style.display = 'block';
        }
        else{
            onglets.item(i).style.display = 'none';
        }
    }
}
ShowFirst(); 


/*
const queryString = window.location.search;
console.log(queryString);
const urlParams = new URLSearchParams(queryString);
const product = urlParams.get('id');
console.log(product);*/