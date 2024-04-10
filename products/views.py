from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('hello guys') 
def mac(request):
    return HttpResponse('new page wizards')

def login(request):
    return HttpResponse('goated type shit')