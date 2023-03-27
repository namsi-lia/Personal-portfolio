from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')

def portfoliodetail(request):
    return render(request,"portfoliodetail.html")