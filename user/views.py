
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
"""

@login_required above methods means a user must be authenticated to access this page.

"""

@login_required
def profile(request):
    return render(request, 'user/profile.html')


@login_required
def profile_edit(request):
    """
    Renders out Profile info, and saves this onto the DB on submit.
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated! ')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'user/edit_profile.html', context)


def page_login(request):
    return render(request, 'user/login.html')


@login_required
def reset(request):
    """
    Self explanatory, logic needs to be built for this at the moment it's non functional.
    """
    return render(request, 'user/password_reset_form.html')


@login_required
def page_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


def register(request):
    """
    Checks if form is valid, then saves and creates a User then redirects to the Login page.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            page_login(user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})






