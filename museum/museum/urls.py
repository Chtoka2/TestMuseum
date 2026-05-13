"""
URL configuration for museum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static

from main import views
from collection import views as collection_views
from news import views as news_views

collection = [
    path("", collection_views.exhibit_list, name="exhibits"),
    path("<int:pk>/", collection_views.exhibit_detail, name="exhibit_detail")
]

news = [
    path('', news_views.article_list, name='article_list'),
    re_path(r'^(?P<slug>[\w-]+)/$', news_views.article_detail, name='news_detail'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("collection/", include(collection)),
    path("news/", include(news)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)