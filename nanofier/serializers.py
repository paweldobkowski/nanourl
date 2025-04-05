from urllib.parse import urlparse

from rest_framework import serializers

from .models import NanoURL

from .utils import generate_unique_short_code


class NanoURLSerializer(serializers.ModelSerializer):
    """
    Serializer for creating the nano ids for long URLs.
    """

    nano_url = serializers.SerializerMethodField()

    class Meta:
        model = NanoURL
        fields = ["original_url", "nano_url"]

    def create(self, validated_data: dict) -> NanoURL:
        validated_data["nano_id"] = generate_unique_short_code()
        return super().create(validated_data)

    def get_nano_url(self, obj: NanoURL) -> str:
        """
        Function builds the whole Nano URL using the ID.
        """

        request = self.context.get("request")
        if request:
            return request.build_absolute_uri(f"/{obj.nano_id}/")
        return f"/{obj.nano_id}/"


class ReverseNanoURLSerializer(serializers.Serializer):
    """
    Serializer for reversing the Nano URL to the original URL.
    """

    nano_url: serializers.URLField = serializers.URLField()
    original_url: serializers.URLField = serializers.URLField(read_only=True)

    def validate(self, attrs: dict) -> dict:
        """
        Extract the Nano URL from nano_url and resolve it.
        """

        url: str = attrs.get("nano_url", "")
        path: str = urlparse(url).path
        nano_id: str = path.strip("/")

        try:
            instance: NanoURL = NanoURL.objects.get(nano_id=nano_id)
        except NanoURL.DoesNotExist:
            raise serializers.ValidationError({"nano_url": "Nano URL not found."})

        attrs["original_url"] = instance.original_url
        return attrs
