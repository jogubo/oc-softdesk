# Generated by Django 4.0.4 on 2022-05-18 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_alter_project_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='project', to=settings.AUTH_USER_MODEL),
        ),
    ]