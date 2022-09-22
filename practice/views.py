from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def challenge(request, month):
    return HttpResponse(month)
