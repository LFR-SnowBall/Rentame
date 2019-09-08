
/** Array con las imagenes a mostrar en la web */

 var imagenes=new Array('img/Casa1.jpg','img/Casa2.jpg','img/Casa3.jpg','img/Casa4.jpg','img/LogoRentame.png');

 /** Funcion para cambiar la imagen */

 function cambiarimagen(){
     
    // obtenemos un numero aleatorio entre 0 y la cantidad de imagenes que hay

     var index=Math.floor((Math.random()*imagenes.length));

     // cambiamos la imagen

     document.getElementById('imagen').src=imagenes[index];

     
 }

/** Función que se ejecuta una vez cargada la página */

onload=function(){
    Estado();
}
function Estado(){
    var estados=['Michoacan','Jalisco'];
    var Michoacan=['Morelia','Patzcuaro'];
    var Jalisco=['Guadalajara'];
    for(var i in Michoacan){document.getElementById('Ciudad').innerHTML+="<option value=''>"+Michoacan[i]+"</option>";
    }
}
function Ciudades(){
    var Etd= document.getElementById('Estado'),
    value=select.value;
    var Michoacan=['Morelia','Patzcuaro'];
    var Jalisco=['Guadalajara'];

    
        for(var i in Michoacan){document.getElementById('Ciudad').innerHTML+="<option value=''>"+Michoacan[i]+"</option>";
    
    }

}
//inicio Carga imagenes
$("#botonera a").click(function(event){
	 
    $("#subir").show("fast");
    
    event.preventDefault();
    
    var hash = this.hash;
    
    $("body").animate({
        
        scrollTop: $(hash).offset().top
       
        }, 400);
    
    });
    
   
   $("#subir a").click(function(event){
    
    $("#subir").hide("fast");
    
    event.preventDefault();
    
    var hash = this.hash;
    
    $("body").animate({
        
        scrollTop: $(hash).offset().top
       
        }, 400);
    
    });
//Fin carga imagenes