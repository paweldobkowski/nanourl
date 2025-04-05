from django.db import models


class NanoURL(models.Model):
    """
    Main app model, stores the original URL and its shortened code.
    """

    nano_id = models.CharField(max_length=10, primary_key=True)
    original_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"ID: {self.nano_id}, for: {self.original_url}"
