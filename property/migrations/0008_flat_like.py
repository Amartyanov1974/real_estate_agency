# Generated by Django 2.2.24 on 2023-06-02 05:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0007_auto_20230601_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='like',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
