from django.shortcuts import render
from django.http import HttpResponse

'''
def home(request):
    return HttpResponse("<h1>Ola Mundo!</h1>")
'''

def home(request):
    return render(request, "fotografia/home.html")