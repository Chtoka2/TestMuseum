from django.shortcuts import render
from django.http import HttpResponse

from news.models import Article

def index(request):
    context = {
        'latest_news': Article.objects.filter(is_published=True).order_by('-published_at')[:5],
    }
    return render(request, 'index.html', context)