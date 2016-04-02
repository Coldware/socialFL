socialModule.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/VLogin', {
                controller: 'VLoginController',
                templateUrl: 'app/ident/VLogin.html'
            }).when('/VPrincipal', {
                controller: 'VPrincipalController',
                templateUrl: 'app/ident/VPrincipal.html'
            }).when('/VRegistro', {
                controller: 'VRegistroController',
                templateUrl: 'app/ident/VRegistro.html'
            });
}]);

socialModule.controller('VLoginController', 
   ['$scope', '$location', '$route', '$timeout', 'flash', 'chatService', 'foroService', 'identService', 'paginasService',
    function ($scope, $location, $route, $timeout, flash, chatService, foroService, identService, paginasService) {
      $scope.msg = '';
      $scope.fLogin = {};

      identService.VLogin().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }


      });
      $scope.VRegistro1 = function() {
        $location.path('/VRegistro');
      };

      $scope.fLoginSubmitted = false;
      $scope.AIdentificar0 = function(isValid) {
        $scope.fLoginSubmitted = true;
        if (isValid) {
          
          identService.AIdentificar($scope.fLogin).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
socialModule.controller('VPrincipalController', 
   ['$scope', '$location', '$route', '$timeout', 'flash', 'ngDialog', 'ngTableParams', 'chatService', 'foroService', 'identService', 'paginasService',
    function ($scope, $location, $route, $timeout, flash, ngDialog, ngTableParams, chatService, foroService, identService, paginasService) {
      $scope.msg = '';
      identService.VPrincipal().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
        
        var VComentario0Data = $scope.res.data0;
        if(typeof VComentario0Data === 'undefined') VComentario0Data=[];
        $scope.tableParams1 = new ngTableParams({
          page: 1,            // show first page
          count: 10           // count per page
        }, {
            total: VComentario0Data.length, // length of data
            getData: function($defer, params) {
              $defer.resolve(VComentario0Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
            }
        });  

      });
      $scope.VLogin0 = function() {
        $location.path('/VLogin');
      };
      $scope.APagina1 = function(idPagina) {
          
        paginasService.APagina({"idPagina":((typeof idPagina === 'object')?JSON.stringify(idPagina):idPagina)}).then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.VContactos2 = function(idUsuario) {
        $location.path('/VContactos/'+idUsuario);
      };
      $scope.VForos3 = function(idUsuario) {
        $location.path('/VForos/'+idUsuario);
      };
      $scope.VComentariosPagina4 = function(idPaginaSitio) {
        $location.path('/VComentariosPagina/'+idPaginaSitio);
      };
      $scope.VComentarioContenido = function(contenido) {
        string = '<div class="ngdialog-message">' + ((typeof contenido === 'object')?JSON.stringify(contenido):contenido) + '</div>';
        ngDialog.open({ scope: $scope, template:  string,
              plain: 'true',
        showClose: true, closeByDocument: true, closeByEscape: true});
      };

    }]);
socialModule.controller('VRegistroController', 
   ['$scope', '$location', '$route', '$timeout', 'flash', 'chatService', 'foroService', 'identService', 'paginasService',
    function ($scope, $location, $route, $timeout, flash, chatService, foroService, identService, paginasService) {
      $scope.msg = '';
      $scope.fUsuario = {};

      identService.VRegistro().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }


      });
      $scope.VLogin1 = function() {
        $location.path('/VLogin');
      };

      $scope.fUsuarioSubmitted = false;
      $scope.ARegistrar0 = function(isValid) {
        $scope.fUsuarioSubmitted = true;
        if (isValid) {
          
          identService.ARegistrar($scope.fUsuario).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
