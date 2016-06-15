//CPF mask using jQuery masked input
$(document).ready(function(){	$("#cpfID").mask("999.999.999-99");});

var sList = [{ID: "111.111.111-11", index: "1"},
             {ID: "000.000.000-00", index: "2"}];

function listVerify() {
    var ID, i, found;
    var out="";

    ID = document.getElementById("cpfID").value;
    sList = sListExC2;
    found = false;
    len = sList.length;
    for (i = 0; i < len; i++) {
        if (sha1(ID) == sList[i].ID){
            found = true;
            out += '<table class="table">\
                    <thead><tr>\
                    <th class="text-center">EE</th>\
                    <th class="text-center">Q1</th>\
                    <th class="text-center">Q2</th>\
                    <th class="text-center">Q3</th>\
                    <th class="text-center">Q4</th>\
                    <th class="text-center">Nota total</th>\
                    </tr></thead>\
                    <tbody>';
            out += "<tr>";
            out += '<td class="text-center">' + sList[i].EE + "</td>";
            out += '<td class="text-center">' + sList[i].std.P1 + "</td>";
            out += '<td class="text-center">' + sList[i].std.P2 + "</td>";
            out += '<td class="text-center">' + sList[i].std.P3 + "</td>";
            out += '<td class="text-center">' + sList[i].std.P4 + "</td>";
            if (sList[i].std.Total >= 7){
                out += '<td class="text-center text-info">' + sList[i].std.Total + "</td>";
            } else {
                out += '<td class="text-center text-danger">' + sList[i].std.Total + "</td>";
            }
            
            out += "</tr></p>";
            out += '</tbody></table>';
        }
    }

    if (!found) out += "CPF não encontrado!";
    
    document.getElementById("listVerifyResult").innerHTML = out;
}


function hash() {
    var ID, i, found;
    var out="";

    initVal = document.getElementById("sha1Hash").value;

    out = sha1(initVal)

    document.getElementById("hashResult").innerHTML = out;
}
