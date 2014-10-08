/**
 * Created by renzo on 10/8/14.
 */

$(document).ready(function(){
    $('button').click(function(){
       console.log('Hello World');
    });

    $('.bt').click(function(evento){
        console.log(evento);
    });

    $('#bt2').click(function(evento){
        console.log('id');
    });
});
