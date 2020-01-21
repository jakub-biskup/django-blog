from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from blog.models import Post
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return render(request, 'users/logout.html')
    else:
        return redirect('blog-home')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,
                                instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/user_profile.html', context)


def community_profile(request, username):
    user = User.objects.get(username=username)

    if user:
        user_posts = Post.objects.filter(author_id=user.id).order_by('-date_posted')
        paginator = Paginator(user_posts, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'c_user': user,
            'page_obj': page_obj,
        }
        return render(request, 'users/community_profile.html', context)
    else:
        return redirect('blog-home')
