# Generated by Django 2.2.24 on 2023-06-01 12:16

from django.db import migrations
from django.db.models import Case, Value, When

def fill_field_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.update(new_building=Case(
        When(construction_year__lt=2015, then=Value(False)),
        When(construction_year__gte=2015, then=Value(True)),
    ))


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_field_new_building),
    ]
