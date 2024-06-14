# from django.shortcuts import render
from django.http import HttpResponse
from .models import  Appointment

# Create your views here.

def create_appointment(request):
    return HttpResponse("I am dummy text!")