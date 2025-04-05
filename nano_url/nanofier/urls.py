from django.urls import path
from .views import CreateNanoURL

urlpatterns = [
    path("nanofy/", CreateNanoURL.as_view(), name="nanofy"),
]
