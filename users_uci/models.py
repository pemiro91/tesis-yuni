import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

from eventos.validators import validate_image_extension

# Create your models here.

PROFILES = (
    ('Estudiante', 'Estudiante'),
    ('Profesor', 'Profesor'),
    ('Administrador', 'Administrador'),
)

CATEGORIES = (
    ('Doctor', 'Doctor'),
    ('Master', 'Master'),
    ('Ingeniero', 'Ingeniero'),
)

YEAR_STUDENT = (
    ('1er', '1er'),
    ('2do', '2do'),
    ('3ro', '3ro'),
    ('4to', '4to'),
    ('5to', '5to'),
)


class User(AbstractUser):
    perfil = models.CharField(max_length=15, choices=PROFILES)
    photo = models.ImageField(upload_to='photo_profile/', null=True, blank=True, validators=[validate_image_extension])
    category = models.CharField(max_length=15, choices=CATEGORIES)
    year_student = models.CharField(max_length=15, choices=YEAR_STUDENT)
    slug = models.SlugField(unique=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.photo.path):
            os.remove(self.photo.path)

        super(User, self).delete(*args, **kwargs)

    def __str__(self):
        return self.first_name
