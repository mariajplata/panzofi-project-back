from django.shortcuts import render
from django.http import HttpResponse

# Login
def index(request):
    return HttpResponse("Login")

