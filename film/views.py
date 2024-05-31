from django.shortcuts import render
from .models import Article
def home__view(request):
    return render(request, 'index.html')


def about__view(request):
    return render(request, 'about.html')


def contact__view(request):
    return render(request, 'contact.html')