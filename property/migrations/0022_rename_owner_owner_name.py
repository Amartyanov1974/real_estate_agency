# Generated by Django 3.2 on 2023-06-05 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0021_alter_complaint_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner',
            new_name='name',
        ),
    ]