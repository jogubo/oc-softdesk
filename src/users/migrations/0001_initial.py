# Generated by Django 4.0.4 on 2022-04-22 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=128)),
                ('last_name', models.CharField(blank=True, max_length=128)),
                ('email', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]