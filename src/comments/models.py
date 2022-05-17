from django.conf import settings
from django.db import models

from issues.models import Issue


class Comment(models.Model):
    description = models.TextField(max_length=2048)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT
    )
    issue = models.ForeignKey(
            Issue,
            on_delete=models.CASCADE,
            related_name='comments')
    created_time = models.DateTimeField(auto_now_add=True)
