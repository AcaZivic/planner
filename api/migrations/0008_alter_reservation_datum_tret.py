# Generated by Django 4.1 on 2022-08-23 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_alter_reservation_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="datum_tret",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 8, 23, 9, 9, 52, 805713, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
