from django.shortcuts import render
from django.http import HttpResponse


def polls(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

# Create your views here.
