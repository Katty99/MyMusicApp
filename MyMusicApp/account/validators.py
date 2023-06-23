from django.core.exceptions import ValidationError


def validate_username(value):
    for symbol in value:
        if not symbol.isalpha() and not symbol.isnumeric() and symbol != '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
