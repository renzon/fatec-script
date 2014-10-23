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
    var $ajaxGif = $('#ajax-gif');

    var $tituloDiv = $('#tituloDiv');

    $ajaxGif.hide();
    var $salvarBtn = $('#salvar-btn');
    var $helpTituloSpan = $('#help-titulo');
    var $corpoTabela = $('#corpo-tabela');

    var adicionarLinha=function adicionarLinha(filme) {
        var linha = '<tr id="tr' + filme.id + '"> <td>' + filme.titulo + '</td>' +
            '<td>' + filme.preco + '</td>' +
            '<td>' + filme.data + '</td>' +
            '<td><button id="bt' + filme.id + '" class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-trash"></i></button>' +
            '</td> </tr>';

        $corpoTabela.prepend(linha);

        var $linhaHtml = $('#tr' + filme.id);

        $linhaHtml.hide();
        $linhaHtml.fadeIn();
        $('#bt' + filme.id).click(function () {
            $linhaHtml.fadeOut();
            $.post('/filmes/rest/delete',{'filme_id':filme.id}).success(function(){
                $linhaHtml.remove();
            }).error(function(){
                alert('Remoção não funcionou');
                $linhaHtml.fadeIn();
            });
        });
    }

    $.get('/filmes/rest').success(function (listaDeFilmes) {
        for (var i = 0; i < listaDeFilmes.length; i += 1) {
            adicionarLinha(listaDeFilmes[i]);
        }

    });

    $salvarBtn.click(function () {
        var filme = {titulo: $tituloInput.val(),
            preco: $precoInput.val(),
            data: $dataInput.val()};

        $ajaxGif.slideDown();
        $salvarBtn.hide();
        var promessa = $.post('/filmes/rest/save', filme);
        promessa.success(function (filme_do_servidor) {
            adicionarLinha(filme_do_servidor);
        });


        promessa.error(function (erros) {
            if (erros.responseJSON != null && erros.responseJSON.titulo != null) {
                $tituloDiv.addClass('has-error');
                $helpTituloSpan.text(erros.responseJSON.titulo);
            }
        });

        promessa.always(function () {
            $ajaxGif.slideUp();
            $salvarBtn.slideDown();
        })
    });

});
