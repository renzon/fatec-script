var filmeModulo = angular.module('filme-modulo', ['filme-servico']);

filmeModulo.directive('filmeForm', [function () {
    return {
        restrict: 'E',
        templateUrl: '/static/filme/html/form.html',
        scope: {},
        controller: function ($scope, $http,FilmeAPI) {
            $scope.filme = {titulo: 'Sonho de Liberdade', preco: '45', data: '02/07/2014'};
            $scope.executandoSalvamento=false;
            console.log();
            $scope.salvar = function () {
                $scope.executandoSalvamento=true;
                var promessa = FilmeAPI.salvar($scope.filme);
                promessa.success(function(filme){
                    console.log(filme);
                    $scope.executandoSalvamento=false;
                });
                promessa.error(function(erros){
                    console.log(erros);
                    $scope.executandoSalvamento=false;
                });
            }
        }
    };
}]);