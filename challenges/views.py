from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

challenges_by_month = {
    "january": "Hit the gym!",
    "february": "Go to the boxing training once a week",
    "march": "Find a girlfriend at least one!",
    "april": "Hit the gym twice a day!",
    "may": "Go to the boxing training twice a week",
    "june": "Find a girlfriend at least three!",
    "july": "Go to the boxing training twice a week",
    "august": "Hit the gym everyday!",
    "september": "Find a girlfriend at least one!",
    "october": "Go to the boxing training twice a month",
    "november": "Go the gym with a friend!",
    "december": "Find a girlfriend at least two!"
}

def index(request):
    months = list(challenges_by_month.keys())
    return render(request,"challenges\index.html", {"months": months})

def month_view(request, month):
    try:
        challenge_text = challenges_by_month[month]
        return render(request, "challenges\challenge.html", {
            "challenge_text": challenge_text,
            "month": month
            })
    except:
        return Http404()

def month_by_number_view(request, month):
    if month > 12:
        return HttpResponseNotFound("We have only 12 months, choose the number more carefully.")
    else:
        month_list = list(challenges_by_month.keys())
        month_world = month_list[month-1]
        redirect_url = reverse("month-challenge", args=[month_world])
        return HttpResponseRedirect(month_world, redirect_url)
