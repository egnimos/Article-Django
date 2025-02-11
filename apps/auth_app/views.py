from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def login(request):
    return render(request, "auth_app/auth.html")


def register(request):
    return render(request, "auth_app/register.html")