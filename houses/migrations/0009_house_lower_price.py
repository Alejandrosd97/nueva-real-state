# Generated by Django 4.0.2 on 2022-11-10 23:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('houses', '0008_house_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='lower_price',
            field=models.ManyToManyField(related_name='interested_in_lower_price', to=settings.AUTH_USER_MODEL),
        ),
    ]
