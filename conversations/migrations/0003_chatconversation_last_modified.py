# Generated by Django 4.0.2 on 2022-11-15 10:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0002_alter_chatconversation_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatconversation',
            name='last_modified',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
