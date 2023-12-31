# Generated by Django 4.0.2 on 2022-11-27 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0013_house_last_modified_house_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='latitude',
            field=models.DecimalField(decimal_places=8, default=40.4165, max_digits=12),
        ),
        migrations.AddField(
            model_name='city',
            name='longitude',
            field=models.DecimalField(decimal_places=8, default=-3.70256, max_digits=12),
        ),
        migrations.AlterField(
            model_name='house',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
