# Generated by Django 3.1 on 2020-08-25 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpi_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('value', models.FloatField()),
                ('rpi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpi_manager.rpi')),
            ],
        ),
    ]
