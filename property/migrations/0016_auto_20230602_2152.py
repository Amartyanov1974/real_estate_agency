# Generated by Django 3.2 on 2023-06-02 18:52

from django.db import migrations


def fill_in_the_links(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    owners = Owner.objects.all()
    for owner in owners.iterator():
        flat = Flat.objects.filter(owner=owner.owner)
        owner.flats.add(*flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20230602_2138'),
    ]

    operations = [
        migrations.RunPython(fill_in_the_links),
    ]
