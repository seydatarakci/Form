from django.urls import path
from contract.models import Contract

from . import views




urlpatterns = [
    
    path('', views.Addcontract, name='Addcontract'),
]