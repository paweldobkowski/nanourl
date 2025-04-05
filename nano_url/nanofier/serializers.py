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
            return request.build_absolute_uri(f"{obj.nano_id}/")
        return f"{obj.nano_id}/"
