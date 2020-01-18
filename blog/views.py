from django.shortcuts import render, redirect
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "About"})


def posts(request, post_title_id):
    posts = Post.objects.all()

    for post in posts:
        title = post.title.lower()
        title = title.replace(' ', '-')

        if title == post_title_id:
            return render(request, 'blog/post.html', {'post': post})

    return redirect('blog-home')
