# Generated by Django 4.1.1 on 2022-09-13 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_alter_reservation_datum_tret_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='datum_tret',
            field=models.DateField(default=datetime.datetime(2022, 9, 13, 17, 47, 30, 160522, tzinfo=datetime.timezone.utc)),
        ),
    ]
