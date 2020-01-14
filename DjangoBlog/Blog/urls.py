from django.urls import path

from .import views

urlmapping = {
    'home': '',
    'about': 'about/'
}

urlpatterns = [
    path(urlmapping['home'], views.home, name='blog-home'),
    path(urlmapping['about'], views.about, name='blog-about')
]