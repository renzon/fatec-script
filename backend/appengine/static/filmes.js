/**
 * Created by renzo on 10/8/14.
 */

$(document).ready(function(){
    var $filmeForm = $('#filme-form');
    $filmeForm.hide();
    $('#mostrar-form-btn').click(function(){
        $filmeForm.slideToggle();
    });


});
