# Generated by Django 4.0.4 on 2022-05-31 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=2048)),
                ('type', models.CharField(choices=[('BE', 'Back-end'), ('FE', 'Front-end'), ('IOS', 'iOS'), ('ANDROID', 'Android')], max_length=128)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
