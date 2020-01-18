from django.urls import path, re_path

from .import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    re_path(r'^posts/([0-9]+)/$', views.posts, name='blog-posts')
]