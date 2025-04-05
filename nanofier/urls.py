from django.urls import path

from .views import CreateNanoURL, ReverseNanoURL

urlpatterns = [
    path("nanofy/", CreateNanoURL.as_view(), name="nanofy"),
    path("resolve/", ReverseNanoURL.as_view(), name="resolve"),
]
