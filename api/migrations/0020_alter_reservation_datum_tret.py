# Generated by Django 4.1.1 on 2022-09-13 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_reservation_datum_tret'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='datum_tret',
            field=models.DateField(default=datetime.datetime(2022, 9, 13, 7, 59, 53, 67578, tzinfo=datetime.timezone.utc)),
        ),
    ]
