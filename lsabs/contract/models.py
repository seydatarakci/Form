from django.db import models
from django.db.models import DateTimeField
from django.forms import ModelForm

from base.models import Firm,Project,Subsidiary
# Create your models here.

class Contract(models.Model):
    firm_name=models.ManyToManyField(Subsidiary,verbose_name= 'Firm Name')
    
    created_time = models.DateTimeField(auto_now_add= True, verbose_name='Eklenme Tarihi')
    
    def __str__(self):
        return str(self.id)
    