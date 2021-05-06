from django import forms
from base.models import Firm,Project,Subsidiary
from django.db.models import DateTimeField
from .models import *


class FirmForm(forms.ModelForm):

    """title= forms.CharField(label='firm Name', max_length=100)
    axcode=forms.CharField(label='Ax Code', max_length=3)
    category =forms.ChoiceField(label= 'Category')"""

    class Meta:
        model = Firm
        fields=('__all__')
                                    