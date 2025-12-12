from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from .exceptions import CustomMiddlewareException

# Create your views here.


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "index.html")


def test_error_404(request):
    raise Http404("Page introuvable pour le test !")


def test_error_perm(request):
    # raise CustomMiddlewareException("Interdit !")
    raise PermissionDenied("interdit !!!")
