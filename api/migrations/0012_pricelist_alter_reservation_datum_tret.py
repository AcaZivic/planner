# Generated by Django 4.1 on 2022-09-05 18:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_alter_reservation_datum_tret"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pricelist",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=None, max_length=2, primary_key=True, serialize=False
                    ),
                ),
                (
                    "pun_naziv",
                    models.TextField(default="naziv tretmana", max_length=60),
                ),
                ("cena_tret", models.IntegerField(default=500)),
            ],
        ),
        migrations.AlterField(
            model_name="reservation",
            name="datum_tret",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 9, 5, 18, 35, 59, 600447, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
