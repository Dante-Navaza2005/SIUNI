from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request): #? the first parameter always has to be a request
    usuarios = Usuario.objects.all()
    context = {'usuarios': usuarios} 
    return render(request, 'homepage.html', context) #? returns the homepage
