from django import forms
from base.models import Firm,Project,Subsidiary
from django.db.models import DateTimeField
import datetime
from .models import *

class ContractForm(forms.ModelForm):

    
    Firm_Name=forms.ModelChoiceField(queryset=Firm.objects.all(),label="Firm Name")
    Limak_Firm=forms.ModelChoiceField(queryset=Firm.objects.all(),label="Limak Firm Name")
    Firm_axcode=forms.ModelChoiceField(queryset=Subsidiary.objects.all(),label="Firm Axcode")
    Limak_axcode=forms.ModelChoiceField(queryset=Subsidiary.objects.all(),label="Limak Firm Axcode")
    created_time = forms.DateTimeField(label='Tarih',widget=forms.SelectDateWidget)
    document=forms.FileField(label='Dosya')
  

    class Meta:
        model = Contract
        fields=("Firm_Name","Limak_Firm","Firm_axcode","Limak_axcode","document")
        

    
            
         
    

        

    
            
         
    
