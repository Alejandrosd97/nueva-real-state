# Generated by Django 4.0.2 on 2022-11-20 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0004_merge_20220515_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.IntegerField(max_length=9, null=True, unique=True),
        ),
    ]