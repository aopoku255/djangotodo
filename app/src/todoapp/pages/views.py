from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def pages(request):
    template = loader.get_template("home.html")
    context = {
        "request": request
    }
    return HttpResponse(template.render(context))

# CONATACTS
def contacts(request):
    return HttpResponse("<h1>Contacts</h1>")

# Create your views here.
