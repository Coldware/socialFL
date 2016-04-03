socialModule.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/VMiPagina/:idUsuario', {
                controller: 'VMiPaginaController',
                templateUrl: 'app/paginas/VMiPagina.html'
            }).when('/VPagina/:idUsuario', {
                controller: 'VPaginaController',
                templateUrl: 'app/paginas/VPagina.html'
            }).when('/VPaginaSitio/:idSitio', {
                controller: 'VPaginaSitioController',
                templateUrl: 'app/paginas/VPaginaSitio.html'
            }).when('/VCrearSitio', {
                controller: 'VCrearSitioController',
                templateUrl: 'app/paginas/VCrearSitio.html'
            });
}]);

socialModule.controller('VMiPaginaController', 
   ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'ngDialog', 'identService', 'paginasService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, ngDialog, identService, paginasService) {
      $scope.msg = '';
      paginasService.VMiPagina({"idUsuario":$routeParams.idUsuario}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }


      });
      $scope.VLogin0 = function() {
        $location.path('/VLogin');
      };
      $scope.VPrincipal1 = function() {
        $location.path('/VPrincipal');
      };
      $scope.VPagina2 = function(idUsuario) {
        $location.path('/VPagina/'+idUsuario);
      };

$scope.__ayuda = function() {
ngDialog.open({ template: 'ayuda_VMiPagina.html',
        showClose: true, closeByDocument: true, closeByEscape: true});
}
    }]);

socialModule.controller('VPaginaController', 
   ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'ngDialog', 'identService', 'paginasService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, ngDialog, identService, paginasService) {
      $scope.msg = '';
      $scope.fPagina = {};

      paginasService.VPagina({"idUsuario":$routeParams.idUsuario}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.titulo != 'Sin Pagina') { // Cambio para que salgan modificaciones 
            $scope.fPagina.titulo = $scope.titulo;
            $scope.fPagina.contenido = $scope.contenido;
        }
        if ($scope.logout) {
            $location.path('/');
        }


      });
      $scope.VLogin0 = function() {
        $location.path('/VLogin');
      };
      $scope.VPrincipal1 = function() {
        $location.path('/VPrincipal');
      };

      $scope.fPaginaSubmitted = false;
      $scope.AModificarPagina0 = function(isValid) {
        $scope.fPaginaSubmitted = true;
        if (isValid) {
          
          paginasService.AModificarPagina($scope.fPagina).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

$scope.__ayuda = function() {
ngDialog.open({ template: 'ayuda_VPagina.html',
        showClose: true, closeByDocument: true, closeByEscape: true});
}
}]);

socialModule.controller('VPaginaSitioController', 
   ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'ngDialog', 'identService', 'paginasService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, ngDialog, identService, paginasService) {
      $scope.msg = '';
      paginasService.VPaginaSitio({"idSitio":$routeParams.idSitio}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }


      });
      $scope.VLogin0 = function() {
        $location.path('/VLogin');
      };
      $scope.VPrincipal1 = function() {
        $location.path('/VPrincipal');
      };
      $scope.VComentariosPagina0 = function(idSitio) {
        $location.path('/VComentariosPagina/'+idSitio);
      };
}]);

socialModule.controller('VCrearSitioController', 
   ['$scope', '$location', '$route', '$timeout', 'flash', '$routeParams', 'ngDialog', 'identService', 'paginasService',
    function ($scope, $location, $route, $timeout, flash, $routeParams, ngDialog, identService, paginasService) {
      $scope.msg = '';
      $scope.fPagina = {};

      paginasService.VCrearSitio().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.titulo != 'Sin Pagina') { // Cambio para que salgan modificaciones 
            $scope.fPagina.titulo = $scope.titulo;
            $scope.fPagina.contenido = $scope.contenido;
        }
        if ($scope.logout) {
            $location.path('/');
        }


      });
      $scope.VLogin0 = function() {
        $location.path('/VLogin');
      };
      $scope.VPrincipal1 = function() {
        $location.path('/VPrincipal');
      };

      $scope.fPaginaSubmitted = false;
      $scope.ACrearSitio0 = function(isValid) {
        $scope.fPaginaSubmitted = true;
        if (isValid) {
          
          paginasService.ACrearSitio($scope.fPagina).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

}]);