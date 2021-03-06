# Generated by Django 3.1 on 2021-04-27 15:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("rpi_manager", "0006_auto_20201220_1538"),
    ]

    operations = [
        migrations.AddField(
            model_name="rpi",
            name="last_connect",
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="ec",
            name="rpi",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ec",
                to="rpi_manager.rpi",
            ),
        ),
        migrations.AlterField(
            model_name="ph",
            name="rpi",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ph",
                to="rpi_manager.rpi",
            ),
        ),
    ]
