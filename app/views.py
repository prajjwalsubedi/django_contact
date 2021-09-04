from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    
 

    context = {
    'contacts': models.Contact.objects.all()
    }
    return render(request,'index.html', context)