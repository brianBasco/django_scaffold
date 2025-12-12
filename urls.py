from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test-error-404/", views.test_error_404, name="test_error_404"),
    path("test-perm/", views.test_error_perm, name="test_perm"),
]
