from django.shortcuts import render
from django.http import HttpResponseRedirect
from base.models import Firm,Project,Subsidiary
from . models import *

from base.firmform import FirmForm


# Create your views here.
def index(request):

    return render(request, 'base/index.html')

def addfirm(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FirmForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            Firm=form.save(commit =False)
            
            Firm.save()
            return render(request, 'base/firmform.html',{'form': form})
    # if a GET (or any other method) we'll create a blank form
    else:
       form = FirmForm()
    
   
    return render(request, 'base/firmform.html',{'form': form})