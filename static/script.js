function numere(input){
    var numere = /[^0-9 .]/gi;
    input.value = input.value.replace(numere,"");
}

function aprindere(){
    document.getElementById("cerc").style.background = '#e8f576';
}

function stingere(){
    document.getElementById("cerc").style.background = 'transparent';
}

function numere_cu_virgula(input){
    var numere = /[^0-9 . ,]/gi;
    input.value = input.value.replace(numere,"");
}