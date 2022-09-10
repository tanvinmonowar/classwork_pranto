from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pranto_file(request):
    return HttpResponse("<h1>Hello Pranto</h1>")
