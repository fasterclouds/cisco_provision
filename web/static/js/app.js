// app.js
$(document).ready(function(){
	
	$.post("./",
    {
        nombre: 	"Franklin",
        apellido: 	"Rincon",
        cedula: 	"v16903045",
        tiempo: 	Date.now()
    },
    function(data, status){
		$("body").fadeIn(1500,function(){			
			// alert("Data: " + data + "\nStatus: " + status);
			console.log(Date.now());
		});
    });
});
