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

    def __str__(self):
        return f'{self.title}'


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
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=12, choices=STATUS)
    assignee_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    description = models.TextField(max_length=2048)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.RESTRICT
    )
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
