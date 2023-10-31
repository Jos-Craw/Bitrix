from django.shortcuts import render
from django.http import HttpResponse
from .models import Application, AdvUser

def index(request):
    apps = Application.objects.all()
    return render(request, 'helper/index.html',{'apps': apps})