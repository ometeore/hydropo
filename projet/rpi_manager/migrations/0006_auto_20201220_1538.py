# Generated by Django 3.1 on 2020-12-20 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpi_manager', '0005_auto_20201215_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterschedule',
            name='rpi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='water', to='rpi_manager.rpi'),
        ),
    ]