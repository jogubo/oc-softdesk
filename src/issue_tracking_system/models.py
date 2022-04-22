from django.conf import settings
from django.db import models


class Project(models.Model):

    PROJECT_TYPES = [
        ('BE', 'Back-end'),
        ('FE', 'Front-end'),
        ('IOS', 'iOS'),
        ('ANDROID', 'Android'),
    ]

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    type = models.CharField(max_length=128, choices=PROJECT_TYPES)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT
    )