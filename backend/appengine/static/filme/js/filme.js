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

            $scope.deletar = function () {
                $scope.apagandoFlag = true;
                FilmeAPI.deletar($scope.filme.id).success(function () {
                    $scope.apagandoFlag = false;
                    if ($scope.filmeDeletado!=null){
                        $scope.filmeDeletado();
                    }
                });
            }
        }
    };
}]);