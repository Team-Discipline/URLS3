# Generated by Django 4.1.1 on 2022-10-02 06:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('access_key', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usualapikey',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]