from django.urls import path, re_path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='news_detail'),
]