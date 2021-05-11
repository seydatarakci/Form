from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from base.models import Firm,Project,Subsidiary
from contract.models import Contract
from . forms import ContractForm
# Create your views here.



def Addcontract(request):
    
    if request.method == 'POST':
        form = ContractForm(request.POST or None, request.FILES or None) 
        
        if form.is_valid():
            Contract=form.save(commit =False)
            document=request.FILES['document']
            Contract.save()
            
            
          
        
    else: 
        form =ContractForm()

    context ={

         'form':form,
        
        }

    return render(request, "contract/addform.html", context)
