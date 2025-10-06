from django.shortcuts import render
from django.http import HttpResponse

def salam(request):
    return HttpResponse('salam chtori!')



