var filmeModulo = angular.module('filme-modulo', ['filme-servico']);

filmeModulo.directive('filmeForm', [function () {
    return {
        restrict: 'E',
        templateUrl: '/static/filme/html/form.html',
        scope: {filmeSalvo: '&'},
        controller: function ($scope, FilmeAPI) {
            $scope.filme = {titulo: 'Sonho de Liberdade', preco: '45a', data: '02/07/2014'};
            $scope.executandoSalvamento = false;
            $scope.erros = {};

            $scope.salvar = function () {
                $scope.executandoSalvamento = true;
                $scope.erros = {};
                var promessa = FilmeAPI.salvar($scope.filme);
                promessa.success(function (filme) {
                    $scope.executandoSalvamento = false;
                    if ($scope.filmeSalvo != null) {
                        $scope.filmeSalvo({'filme': filme})
                    }
                });
                promessa.error(function (erros) {
                    $scope.erros = erros;
                    $scope.executandoSalvamento = false;
                });
            }
        }
    };
}]);

filmeModulo.directive('filmeLinha', [function () {
    return {
        restrict: 'A',
        replace: true,
        templateUrl: '/static/filme/html/linha.html',
        scope: {
            filme: '=',
            filmeDeletado: '&'
        },
        controller: function ($scope, FilmeAPI) {
            $scope.apagandoFlag = false;
            $scope.editandoFlag = false;
            $scope.filmeEdicao={};
            $scope.deletar = function () {
                $scope.apagandoFlag = true;
                FilmeAPI.deletar($scope.filme.id).success(function () {
                    $scope.apagandoFlag = false;
                    if ($scope.filmeDeletado != null) {
                        $scope.filmeDeletado();
                    }
                });
            }

            function copiarFilme(origem, destino){
                destino.id=origem.id;
                destino.data=origem.data;
                destino.titulo=origem.titulo;
                destino.preco=origem.preco;

            }

            $scope.entrarModoEdicao = function () {
                $scope.editandoFlag = true;
                copiarFilme($scope.filme, $scope.filmeEdicao);
            };

            $scope.sairModoEdicao = function () {
                $scope.editandoFlag = false;
            };

            $scope.editar=function (){
                FilmeAPI.editar($scope.filmeEdicao).success(function(filmeServidor){
                    copiarFilme(filmeServidor,$scope.filme);
                    $scope.editandoFlag = false;

                });
            }
        }
    };
}]);