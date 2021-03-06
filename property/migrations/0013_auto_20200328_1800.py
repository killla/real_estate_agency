# Generated by Django 2.2.4 on 2020-03-28 15:00

from django.db import migrations

def owners_with_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        owner = Owner.objects.get_or_create(name=flat.owner, phone=flat.owners_phonenumber)
        owner.flats.add(flat)
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20200328_1759'),
    ]

    operations = [
        migrations.RunPython(owners_with_flats),
    ]
