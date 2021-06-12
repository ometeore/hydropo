# Generated by Django 3.1 on 2021-04-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpi_manager', '0007_auto_20210427_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpi',
            name='is_conected',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rpi',
            name='md5_name',
            field=models.CharField(default='group0', max_length=200),
            preserve_default=False,
        ),
    ]
