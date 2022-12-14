# Generated by Django 4.1 on 2022-09-06 08:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0014_alter_pricelist_id_alter_reservation_datum_tret"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pricelist", options={"ordering": ["id", "cena_tret"]},
        ),
        migrations.AddField(
            model_name="reservation",
            name="cena_izabranog_tretmana",
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="datum_tret",
            field=models.DateField(
                default=datetime.datetime(
                    2022, 9, 6, 8, 8, 54, 323490, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="izbor_tretmana",
            field=models.CharField(
                choices=[
                    ("DG", "Depilacija celih grudi"),
                    ("DL1", "Depilacija celih leđa"),
                    ("DL2", "Depilacija pola leđa"),
                    ("DN", "Nausnice"),
                    ("DN1", "Depilacija hladnim voskom celih nogu"),
                    ("DN2", "Depilacija pola nogu"),
                    ("DO", "Obrve"),
                    ("DR1", "Depilacija celih ruku"),
                    ("DR2", "Depilacija pola ruku"),
                    ("EM", "Manikir"),
                    ("EP", "Estetski pedikir"),
                    ("GL", "Gel – lak"),
                    ("GS1", "Granulom sanacije I stepena"),
                    ("GS2", "Granulom sanacije II stepena"),
                    ("GS3", "Granulom sanacije III stepena obostran"),
                    ("ID", "Intimna depilacija"),
                    ("LN", "Lakiranje na nogama"),
                    ("LTG", "Laserski tretman gljivično obolelih noktiju"),
                    ("LTS", "Laserski tretman sportskih povreda"),
                    ("MHP", "Medicinsko – hirurški pedikir"),
                    ("MP", "Medicinski pedikir"),
                    ("PTP", "Pola tretmana pedikira"),
                    ("PTR", "Parafinski tretman ruku"),
                    ("PTS", "Parafinski tretman stopala"),
                    ("RG", "Revizija granuloma"),
                    ("RUN", "Revizija uraslog nokta"),
                    ("RZ", "Revizija žulja"),
                    ("SGM", "Skidanje gel - laka sa manikirom"),
                    ("SGP", "Skidanje gel - laka (Pedikir)"),
                    ("SM", "Spa manikir"),
                    ("SN", "Skidanje nadogradnje"),
                    ("SNP", "Sečenje noktiju na nogama"),
                    ("SP", "Spa pedikir"),
                    ("SZ", "Obrada i sanacija žulja na stopalu/prstima"),
                    ("SZ2", "Obrada i sanacija 2 i više žulja na stopalu/prstima"),
                    ("UN1", "Urastao nokat – sanacija jedne strane"),
                    ("UN2", "Urastao nokat – sanacija obe strane"),
                    ("UN3", "Urastao nokat – sanacija više strana"),
                ],
                default="MP",
                max_length=3,
            ),
        ),
    ]
