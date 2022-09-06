from django.urls import path
from . import views


urlpatterns = [
    path('',views.getRoutes),
    path('reservations/',views.getReservations),
    path('pricelist/',views.getPricelist),

    path('reservations/create/',views.createReservation),
    path('pricelist/create',views.createPricelistItem),

    path('reservations/<str:pk>/update/',views.updateReservation),
    path('pricelist/<str:pk>/update',views.updatePricelistItem),

    path('reservations/<str:pk>/delete/',views.deleteReservation),

    path('reservations/<str:pk>/',views.getReservation),
    path('pricelist/<str:pk>/',views.getPricelistItem), 
    
]