# from django.shortcuts import render
# Create your views here.

# from django.http import JsonResponse

from ast import Try
from asyncio.windows_events import NULL
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pricelist, Reservation
from .serializers import ReservationSerializer,PricelistSerializer
from api import serializers


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint':'/reservations/',
            'method':'GET',
            'ime_klijenta': '',
            'izbor_radnika':'',
            'izbor_tretmana':'',
            'cena_izabranog_tretmana':0,
            'napomena':'',
            'datum_tret': NULL,
            'poc_tret': None,
            'kraj_tret': None,
            'desciption':'Returns an array of reservations'
        },
        {
            'Endpoint':'/reservations/id',
            'method':'GET',
            'ime_klijenta': '',
            'izbor_radnika':'',
            'izbor_tretmana':'',
            'cena_izabranog_tretmana':0,
            'napomena':'',
            'datum_tret': NULL,
            'poc_tret': None,
            'kraj_tret': None,
            'desciption':'Returns a single note object'
        },
        {
            'Endpoint':'/reservations/create',
            'method':'POST',
            'ime_klijenta': {'ime_klijenta':""},
            'izbor_radnika':{'izbor_radnika':""},
            'izbor_tretmana':{'izbor_tretmana':""},
            'cena_izabranog_tretmana': {'cena_izabranog_tretmana':""},
            'napomena':{'napomena':""},
            'datum_tret': {'datum_tret':""},
            'poc_tret': {'poc_tret':""},
            'kraj_tret': {'kraj_tret':""},
            'desciption':'Creates new reservation with data sent in post request'
        },
        {
            'Endpoint':'/reservations/id/update',
            'method':'PUT',
            'ime_klijenta': {'ime_klijenta':""},
            'izbor_radnika':{'izbor_radnika':""},
            'izbor_tretmana':{'izbor_tretmana':""},
            'cena_izabranog_tretmana': {'cena_izabranog_tretmana':""},
            'napomena':{'napomena':""},
            'datum_tret': {'datum_tret':""},
            'poc_tret': {'poc_tret':""},
            'kraj_tret': {'kraj_tret':""},
            'desciption': 'Update an existing note with data sent in put request'
        },
        {
            'Endpoint':'/reservation/id/delete',
            'method':'DELETE',
            'ime_klijenta': {'ime_klijenta':""},
            'izbor_radnika':{'izbor_radnika':""},
            'izbor_tretmana':{'izbor_tretmana':""},
            'cena_izabranog_tretmana': {'cena_izabranog_tretmana':""},
            'napomena':{'napomena':""},
            'datum_tret': {'datum_tret':""},
            'poc_tret': {'poc_tret':""},
            'kraj_tret': {'kraj_tret':""},
            'desciption':'Deletes existing reservation'
        },
        {
            'Endpoint':'/pricelist/',
            'method':'GET',
            'pun_naziv':'',
            'cena_tret':'',
            'desciption':'Returns an array of pricelist items'
        },
        {
            'Endpoint':'/pricelist/id',
            'method':'GET',
            'pun_naziv':'',
            'cena_tret':'',
            'desciption':'Returns a single item of pricelist items'
        },
        {
            'Endpoint':'/pricelist/create',
            'method':'POST',
            'id':{'id':''},
            'pun_naziv':{'pun_naziv':''},
            'cena_tret':{'cena_tret':''},
            'desciption':'Create new pricelist item'
        },
        {
            'Endpoint':'/pricelist/id/update',
            'method':'PUT',
            'pun_naziv':{'pun_naziv':''},
            'cena_tret':{'cena_tret':''},
            'desciption':'Update pricelist item !'
        }
    ]
    # Safe must be false
    # return JsonResponse(routes, safe=False)

    return Response(routes)

@api_view(['GET'])
def getReservations(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getReservation(request,pk):
    try:
        reservation = Reservation.objects.get(id=pk)
        serializer = ReservationSerializer(reservation, many=False)
        return Response(serializer.data)
    except:
        return Response("Greska rezervacija ne postoji ")
    

@api_view(['POST'])
def createReservation(request):
    data = request.data 
    reservation = Reservation.objects.create(
        ime_klijenta = data['ime_klijenta'],
        izbor_radnika = data['izbor_radnika'],
        izbor_tretmana= data['izbor_tretmana'],
        cena_izabranog_tretmana = data['cena_izabranog_tretmana'],
        napomena = data['napomena'],
        datum_tret = data['datum_tret'],
        poc_tret = data['poc_tret'],
        kraj_tret = data['kraj_tret']
    )
    serializer = ReservationSerializer(reservation,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateReservation(request,pk):
    try:
        reservation = Reservation.objects.get(id=pk)
        serializer = ReservationSerializer(reservation,data=request.data)
    except:
        return Response("Greska rezervacija ne postoji sa tim id-ijem.")
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteReservation(request,pk):
    try: 
        reservation=Reservation.objects.get(id=pk)
        reservation.delete()
    except:
        return Response("Greska rezervazija ne postoji sa tim id-ijem !!!")
    return Response("Reservation was deleted!")


@api_view(['GET'])
def getPricelist(request):
    pricelist = Pricelist.objects.all()
    serializer = PricelistSerializer(pricelist, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPricelistItem(request,pk):
    try:
        pricelist = Pricelist.objects.get(id=pk)
        serializer = PricelistSerializer(pricelist, many=False)
        return Response(serializer.data)
    except:
        return Response("Greska stavka sa tim id-ijem ne postoji !")

@api_view(['POST'])
def createPricelistItem(request):
    data = request.data 
    pricelist = Pricelist.objects.create(
        id = data['id'],
        cena_tret = data['cena_tret'],
        pun_naziv = data['pun_naziv']
    )
    serializer = PricelistSerializer(pricelist,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updatePricelistItem(request,pk):
    try:
        pricelist = Pricelist.objects.get(id=pk)
        serializer = PricelistSerializer(pricelist,data=request.data)
    except:
        return Response("Greska rezervacija ne postoji sa tim id-ijem.")
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)