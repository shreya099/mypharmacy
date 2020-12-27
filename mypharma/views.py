from django.shortcuts import render
from django.http import HttpResponse
from .models import medii,medo

# Create your views here.
def index(request):
    medi=medii.objects.all()
    me=medo.objects.all()

    return render(request,'home.html',{'medi':medi,'me':me})
