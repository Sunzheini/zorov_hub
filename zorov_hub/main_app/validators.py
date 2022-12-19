from django.core.exceptions import ValidationError


def some_validator(value):
    if value < 0:
        raise ValidationError(f'{value} is less than 0')


def validate_text(value):
    if '_' in value:
        raise ValidationError('there is a `_` in the word')


def validate_profile_name(value):
    for ch in value:
        if ch == ' ':
            raise ValidationError('there is a black space in the profile name')
