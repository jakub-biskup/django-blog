from django.shortcuts import render
from . import urls


posts = [
    {
        'author': 'Jakub Biskup',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 13, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 14, 2020'
    }
]


def home(request):
    context = {
        'posts': posts,
        'urls': urls.urlmapping}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "About"})
