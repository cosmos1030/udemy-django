from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

mydic = {
    'january': "go home",
    "february": "watch movies"
}

# Create your views here.
def index(request):
    return HttpResponse("hello")

def num_month(request, month):
    months = list(mydic.keys())
    return HttpResponseRedirect(months[month-1])

def month(request, month):
    try:
        todo = mydic[month]
        return HttpResponse(todo)
    except:
        return HttpResponseNotFound("error")
