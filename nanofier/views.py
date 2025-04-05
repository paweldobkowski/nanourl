from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import NanoURL

from .serializers import NanoURLSerializer, ReverseNanoURLSerializer


class CreateNanoURL(CreateAPIView):
    """
    Function that handles POST request and responds with the Nano URL.
    """

    queryset = NanoURL.objects.all()
    serializer_class = NanoURLSerializer


class ReverseNanoURL(GenericAPIView):
    """
    Function that handles POST request, reverses the Nano URL to original URL.
    """

    serializer_class = ReverseNanoURLSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=HTTP_200_OK)
