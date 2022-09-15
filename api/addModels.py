
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

pom_radnici = None
svi_radnici = None
izb_pom = None
def get_users(): 
    pom_radnici = get_user_model()
    svi_radnici = [x['username'] for x in[a for a in pom_radnici.objects.values('username')]]
    izb_pom = [(y[0]+str(x),y)for x,y in enumerate(svi_radnici)]
    return izb_pom

def get_users_id():
    pom_radnici = get_user_model()
    svi_radnici = [x['username'] for x in[a for a in pom_radnici.objects.values('username')]]
    izb_pom = [(y[0]+str(x),y)for x,y in enumerate(svi_radnici)]
    id_radnika = [x for x,y in izb_pom]
    return id_radnika

def get_users_name():
    pom_radnici = get_user_model()
    svi_radnici = [x['username'] for x in[a for a in pom_radnici.objects.values('username')]]
    return svi_radnici