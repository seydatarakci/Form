from django.urls import path
from contract.models import Contract

from . import views




urlpatterns = [
    
    path('', views.Addcontract, name='Addcontract'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
