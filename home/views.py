from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

def home(request):
    geners = Category.objects.all()
    context = {
        'geners' : geners,
    }
    return render(request, 'home/index.html', context)