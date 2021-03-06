"""djangonautic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views # import the views functions from current directory
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # lets us append to utlpatterns to get static files
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('about/', views.about, name='about'), # the path function takes two parameters
    path('', article_views.article_list, name='homepage'), # 1. URL-pattern and 2. function from views
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls'))
]


urlpatterns += staticfiles_urlpatterns() # checks debug-mode and appends to urlpatters
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)