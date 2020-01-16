from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has bee created! You are now able to log in.')
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
    return render(request, 'users/profile.html')
