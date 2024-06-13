# from django.shortcuts import render, redirect, get_object_or_404, reverse
# from django.views import generic, View
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Day

#create your views here

def  day_of_week(request):
    return HttpResponse("This is dummy text!")


