from django.db import models
from django.conf import settings

from projects.models import Project


class Contributor(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_contributor',
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='project_contributor',
    )
