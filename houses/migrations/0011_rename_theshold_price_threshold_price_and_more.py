# Generated by Django 4.0.2 on 2022-11-11 00:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('houses', '0010_theshold_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='theshold_price',
            new_name='Threshold_price',
        ),
        migrations.RemoveField(
            model_name='house',
            name='lower_price',
        ),
    ]
