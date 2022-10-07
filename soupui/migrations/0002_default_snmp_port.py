# Generated by Django 4.1.1 on 2022-10-07 11:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("soupui", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="device",
            name="port",
            field=models.IntegerField(
                default=161,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(65535),
                ],
            ),
        ),
    ]
