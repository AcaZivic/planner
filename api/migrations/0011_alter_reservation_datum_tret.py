# Generated by Django 4.1 on 2022-09-05 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0010_alter_reservation_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="datum_tret",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 9, 5, 18, 10, 53, 567867, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
