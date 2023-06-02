# Generated by Django 3.2 on 2023-06-02 07:14

from django.db import migrations
import phonenumbers
from django.db.models import Case, Value, When, F

def valid_number(number):
    try:
        phonenumber = phonenumbers.parse(number, 'RU')
    except phonenumbers.phonenumberutil.NumberParseException:
            return None
    return phonenumbers.is_valid_number(phonenumber)

def copy_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    #Flat.objects.filter(valid_number(owners_phonenumber)).update(phonenumbers.format_number(phonenumbers.parse(owners_phonenumber, 'RU'), phonenumbers.PhoneNumberFormat.E164))


    #Flat.objects.filter(valid_number(F('owners_phonenumber'))).update(phonenumbers.format_number(phonenumbers.parse(F('owners_phonenumber'), 'RU'), phonenumbers.PhoneNumberFormat.E164))


    #Flat.objects.update(owner_pure_phone=Case(When(valid_number(F('owners_phonenumber')),
    #        then=Value(phonenumbers.format_number(phonenumbers.parse(F('owners_phonenumber', 'RU')), phonenumbers.PhoneNumberFormat.E164))
    #        )))

    for flat in Flat.objects.all():
        if valid_number(flat.owners_phonenumber):
            flat.owner_pure_phone = phonenumbers.format_number(phonenumbers.parse(flat.owners_phonenumber,
                                                               'RU'), phonenumbers.PhoneNumberFormat.E164)
            flat.save()



class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_alter_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(copy_number),
    ]