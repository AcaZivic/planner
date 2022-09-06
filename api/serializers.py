from rest_framework.serializers import ModelSerializer
from .models import Reservation,Pricelist

class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class PricelistSerializer(ModelSerializer):
    class Meta:
        model = Pricelist
        fields = '__all__'