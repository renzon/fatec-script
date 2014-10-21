/**
 * Created by renzo on 10/8/14.
 */

$(document).ready(function () {
    var $filmeForm = $('#filme-form');
    $filmeForm.hide();
    $('#mostrar-form-btn').click(function () {
        $filmeForm.slideToggle();
    });


    var $tituloInput = $('#tituloInput');
    var $precoInput = $('#precoInput');
    var $dataInput = $('#dataInput');
    $tituloInput.val('Sonho de Liberdade');
    var $ajaxGif=$('#ajax-gif');

    var $tituloDiv=$('#tituloDiv');

    $ajaxGif.hide();
    var $salvarBtn = $('#salvar-btn');
    $salvarBtn.click(function () {
        var filme = {titulo: $tituloInput.val(),
            preco: $precoInput.val(),
            data: $dataInput.val()};

        $ajaxGif.slideDown();
        $salvarBtn.hide();
        var promessa=$.post('/filmes/rest/save',filme);
        promessa.success(function(filme_do_servidor){
            console.log(filme_do_servidor);
        });



        promessa.error(function(erros){
            console.log(erros);
            if (erros.titulo!=null){
                $tituloDiv.addClass('has-errors');
            }
        });

        promessa.always(function(){
            $ajaxGif.slideUp();
            $salvarBtn.slideDown();
        })
    });

});
