
function validaDatas(){

    var dataInicial = new Date($("input[name='data_inicio']").val());
    
    var dataFinal = new Date($("input[name='data_termino']").val());

    if (!dataInicial || !dataFinal) return false;
    
    if (dataInicial >= dataFinal) {
        alert("Data incorreta!");
        return false;
    } 
    else {
        alert("Data Correta!");
        return true
    }
}