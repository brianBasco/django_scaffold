from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponse
from django.shortcuts import render

from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import render
from .exceptions import CustomMiddlewareException


# Exemple de middleware retournant le message d'erreur lors d'une exception levée avec Htmx
class ExceptionHandlingMiddleware:
    """Handle uncaught exceptions instead of raising a 500.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if isinstance(exception, CustomMiddlewareException):
            # Show warning in admin using Django messages framework
            # messages.warning(request, str(exception))
            # Or you could return json for your frontend app
            # return JsonResponse({'error': str(exception)})
            return self._htmx_error(request, 403, str(exception))

        elif isinstance(exception, PermissionDenied):
            return self._htmx_error(request, 503, str(exception))

        elif isinstance(exception, Http404):
            return self._htmx_error(request, 404, str(exception))

        return None  # Middlewares should return None when not applied

    def _htmx_error(self, request, status, message):
        # Si la requête ne vient PAS de HTMX → laisser Django gérer
        print('capturé par le middleware')
        if request.headers.get("HX-Request") != "true":
            raise

        # response = render(request, "partials/error_global.html", {
        #    "message": message
        # })
        # print(message)
        # response.status_code = status
        # Pour forcer le swap :
        # response.status_code = 200
        # response["HX-Retarget"] = "#modal-errors"
        # response["HX-Reswap"] = "innerHTML"
        # return response
        return HttpResponse(f'{status} : {message}', status=status)
