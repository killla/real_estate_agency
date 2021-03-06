# Generated by Django 2.2.4 on 2020-03-28 03:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_claim'),
    ]

    operations = [
        migrations.AddField(
            model_name='claim',
            name='flat',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='property.Flat', verbose_name='Квартира, на которую пожаловались'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='claim',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
    ]
