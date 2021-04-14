from django.shortcuts import render
from django.http import HttpResponse
from .models import Genre

def home(request):
    geners = Genre.objects.all()
    context = {
        'geners' : geners,
    }
    return render(request, 'home/index.html', context)