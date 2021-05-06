from django.urls import path
from tender.models import Tender,Offer
from . import views

urlpatterns = [
    path('', views.tender, name='tender'),
]