import os
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Extención invalida.')


def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Extención invalida.')


def validate_result(value):
    ext = value  # [0] returns path+filename
    valid_results = ['Mención', 'Destacado', 'Relevante']
    if not ext in valid_results:
        raise ValidationError('Resultado invalido.')
