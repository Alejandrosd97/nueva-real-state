# Generated by Django 4.0.2 on 2022-05-21 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('houses', '0004_alter_housepictures_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='likes',
            field=models.ManyToManyField(related_name='liked_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='house',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
