# Generated by Django 4.1 on 2022-08-23 05:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_alter_reservation_options_remove_reservation_created_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="reservation", options={"ordering": ["-datum_tret", "-vreme_tret"]},
        ),
        migrations.AlterField(
            model_name="reservation",
            name="datum_tret",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 8, 23, 5, 54, 57, 876242, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="izbor_radnika",
            field=models.CharField(
                choices=[("A0", "Andjela"), ("S1", "Suza")], default="A0", max_length=2
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="vreme_tret",
            field=models.CharField(
                choices=[
                    ("008", datetime.time(8, 0)),
                    ("108", datetime.time(8, 30)),
                    ("209", datetime.time(9, 0)),
                    ("309", datetime.time(9, 30)),
                    ("410", datetime.time(10, 0)),
                    ("510", datetime.time(10, 30)),
                    ("611", datetime.time(11, 0)),
                    ("711", datetime.time(11, 30)),
                    ("812", datetime.time(12, 0)),
                    ("912", datetime.time(12, 30)),
                    ("1013", datetime.time(13, 0)),
                    ("1113", datetime.time(13, 30)),
                    ("1214", datetime.time(14, 0)),
                    ("1314", datetime.time(14, 30)),
                    ("1415", datetime.time(15, 0)),
                    ("1515", datetime.time(15, 30)),
                    ("1616", datetime.time(16, 0)),
                    ("1716", datetime.time(16, 30)),
                    ("1817", datetime.time(17, 0)),
                    ("1917", datetime.time(17, 30)),
                    ("2018", datetime.time(18, 0)),
                    ("2118", datetime.time(18, 30)),
                    ("2219", datetime.time(19, 0)),
                    ("2319", datetime.time(19, 30)),
                    ("2420", datetime.time(20, 0)),
                ],
                default="008",
                max_length=4,
            ),
        ),
    ]
