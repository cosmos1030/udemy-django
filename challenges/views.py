from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    'january': "Go for a walk",
    'february': 'get out of here',
    'march': 'go home',
    'april': 'study programming'
}

# Create your views here.
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/"+redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("this month is not supported")