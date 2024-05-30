from django.shortcuts import render
from .models import Article
# Create your views here.
def home__view(request):
    films = Article.objects.all()
    return render(request, 'index.html', {'films': films})