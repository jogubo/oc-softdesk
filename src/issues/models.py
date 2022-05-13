from django.conf import settings
from django.db import models

from projects.models import Project


class Issue(models.Model):
    TAG = [
        ('BUG', 'Bug'),
        ('ENHANCEMENT', 'Amélioration'),
        ('TASK', 'Tâche'),
    ]

    PRIORITY = [
        ('HIGH', 'Élevée'),
        ('NORMAL', 'Normal'),
        ('LOW', 'Faible'),
    ]

    STATUS = [
        ('TO_DO', 'À faire'),
        ('IN_PROGRES', 'En cours'),
        ('DONE', 'Terminé'),
    ]

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    tag = models.CharField(max_length=12, choices=TAG)
    priority = models.CharField(max_length=12, choices=PRIORITY)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='issue_related'
    )
    status = models.CharField(max_length=12, choices=STATUS)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='issue_created_by'
    )
    assignee_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name='issue_assigned_to'
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
