from django import forms
from base.models import Firm,Project,Subsidiary
from django.db.models import DateTimeField
import datetime
from .models import *

class ContractForm(forms.ModelForm):

    
    firm_name=forms.CharField(label= 'Firm_Name ',max_length=80)
  
    axcode=forms.CharField(label= 'AxCode',max_length=3)

    created_time = forms.DateTimeField(label='Tarih',widget=forms.SelectDateWidget)


    

    class Meta:
        model = Contract
        fields=('__all__')
        

    
            
         
    
