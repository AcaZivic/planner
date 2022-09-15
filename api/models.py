from calendar import SATURDAY
from dataclasses import asdict
from datetime import date, datetime,time
from inspect import classify_class_attrs
from locale import normalize
from multiprocessing.sharedctypes import Value
from ntpath import join
from pyexpat import model
from re import A
from tokenize import group
from django.db import models
from enum import Enum
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from . import addModels

medicinski_pedikir = "MP"
medicinsko_hiruski_pedikir = "MHP"
estetski_pedikir = "EP"
spa_pedikir = "SP"
pola_tretmana_pedikira = "PTP"
secenje_noktiju_na_nogama = "SNP"
granulom_sanacije_I_stepen = "GS1"
granulom_sanacije_II_stepen = "GS2"
granulom_sanacije_III_stepen = "GS3"
revizija_granuloma = "RG"
urasao_nokat_jedna_strana = "UN1"
urasao_nokat_obe_strane = "UN2"
urasao_nokat_vise_strana = "UN3"
revizija_uraslog_nokta = "RUN"
sanacija_zulja_stopala_prsti = "SZ"
revizija_zulja = "RZ"
sanacija_2ilivise_zulja_stopala_prsti = "SZ2"
lakiranje_na_nogama="LN"
parafinski_tretman_stopala="PTS"
gel_lak= "GL"
laserski_tretman_gljivicno_obolelih_noktiju = 'LTG'
laserski_tretman_sportskih_povreda = "LTS"
estetski_manikir = "EM"
spa_manikir= "SM"
parafinski_tretman_ruku = "PTR"
depilacija_hladnim_voskom_celih_nogu="DN1"
depilacija_hladnim_voskom_pola_nogu="DN2"
depilacija_celih_ruku = "DR1"
depilacija_pola_ruku = "DR2"
depilacija_celih_ledja = "DL1"
depilacija_pola_ledja = "DL2"
depilacija_celih_grudi = "DG"
intimna_depilacija="ID"
nausnice = "DN"
obrve = "DO"
skidanje_nadogradnje="SN"
skidanje_gel_laka_pedikir="SGP"
skidanje_gel_laka_manikir="SGM"


# Create your models here.
class Pricelist(models.Model):
    
    # ATTRIBUTES
    id = models.CharField(
        max_length=3,
        default= None,
        primary_key=True
    )
    pun_naziv = models.TextField(default="naziv tretmana",max_length=60)
    cena_tret = models.IntegerField(default=500)


    # METHODS

    def get_all_pricelist(self):
        query_pricelist = self._meta.model.objects.values('id','pun_naziv','cena_tret')
        return query_pricelist

    def __str__(self):
        # return f"{Reservation.get_all_reservations(Reservation)}"
        return f"{self.id} - {self.pun_naziv} - {self.cena_tret}"
    
    def get_all_tretmans():
        niz = []
        for x in Pricelist.get_all_pricelist(Pricelist):
            niz.append((x['id'],x['pun_naziv']))
        return niz
    
    # ORDERING
    class Meta:
        ordering = ['id','cena_tret']


    
class Reservation(models.Model):
    
    
    # IME KLIJENTA ATRIBUT
    ime_klijenta = models.TextField(
        max_length=25,
        blank=False
    )

    # IZBOR RADNIKA ATRIBUT (
    # Uzimamo usernameove svih korisnika  
    

    izbor_radnika = models.CharField(
        max_length=2,
        choices=addModels.get_users(),
        default=addModels.get_users_id()[0],
    )
    # IZBOR TRETMANA ATRIBUT
    
    izbor_tretmana = models.CharField(
        choices= Pricelist.get_all_tretmans() ,
        default='MP',
        max_length=3
    )

    # CENA ATRIBUT
    
    cena_izabranog_tretmana = models.IntegerField(
        default=1000,
        blank=False
    )


    # NAPOMENA ATRIBUT
    napomena = models.TextField(
        max_length=100,
        blank=True
    )

    # Datum ATRIBUT
    datum_tret = models.DateField(
        default = now()
    )
    poc_tret = models.TimeField(
        default= time(8,0),
        blank=False
    )
    kraj_tret = models.TimeField(
        default= time(8,30),
        blank=False
    )
    
    
    # METODE
    # def get_all_staff(self):
    #     return self.izb_pom

    def get_all_reservations(self):
        query_reservation = self._meta.model.objects.values('id','izbor_tretmana','datum_tret','poc_tret','kraj_tret')
        return query_reservation

    def __str__(self):
        pom = [y for x,y in Pricelist.get_all_tretmans() if x==self.izbor_tretmana]
        pom2 = [y for x,y in addModels.get_users() if x==self.izbor_radnika]

        # {self.svi_radnici} {self.id_radnika[0]} } {str(pom2[0])} - {vreme_lista(self.pom_sati,self.pom_min)} - {Pricelist.get_all_pricelist(Pricelist)} -{dict(self.get_all_staff())} {pom2[0]} 
        return f" {str(pom[0])} - {self.ime_klijenta} - {self.napomena[0:20]} -  {pom2} - {addModels.get_users()} "
    

    class Meta:
        ordering = ['-datum_tret','-poc_tret']
