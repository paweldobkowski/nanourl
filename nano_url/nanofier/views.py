from rest_framework.generics import CreateAPIView

from .models import NanoURL

from .serializers import NanoURLSerializer


class CreateNanoURL(CreateAPIView):
    """
    Function that handles POST request and responds with the Nano URL.
    """

    queryset = NanoURL.objects.all()
    serializer_class = NanoURLSerializer
