from random import choices
from string import ascii_letters, digits

from .models import NanoURL


def generate_unique_short_code(length: int = 5) -> str:
    """
    Generates a unique nano id for long urls provided by user.
    """

    chars = ascii_letters + digits
    while True:
        nano_id = "".join(choices(population=chars, k=length))
        if not NanoURL.objects.filter(nano_id=nano_id).exists():
            return nano_id
