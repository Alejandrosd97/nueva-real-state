# Generated by Django 4.0.2 on 2022-11-20 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0005_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]