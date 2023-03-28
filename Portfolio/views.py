from django.shortcuts import render 
from .models import portfolioDetails
# Create your views here.

def index(request):

    jobs=portfolioDetails.objects.all()

    return render(request, 'index.html', {'jobs':jobs})

