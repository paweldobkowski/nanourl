from rest_framework import serializers

from .models import NanoURL

from .utils import generate_unique_short_code


class NanoURLSerializer(serializers.ModelSerializer):
    """
    Serializer for creating the nano ids for long URLs.
    """

    nano_id = serializers.CharField(read_only=True)

    class Meta:
        model = NanoURL
        fields = ["original_url", "nano_id"]

    def create(self, validated_data: dict) -> NanoURL:
        validated_data["nano_id"] = generate_unique_short_code()
        return super().create(validated_data)
