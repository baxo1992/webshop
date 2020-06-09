from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, NewUserForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,
                                username=username,
                                password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, f"You are now logged in as {username}")
                    return redirect("shop:product_list")
                else:
                    messages.info(request, 'Disabled account')
                    return render(request, "login.html")
            else:
                messages.error(request, 'Invalid login')
                return render(request, "login.html")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_request(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("shop:product_list")


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'New Account Created: {username}')
            return redirect("shop:product_list")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request, "registration.html", {'form': form})


@login_required
def dashboard(request):
    return render(request,
                  'dashboard.html',
                  {'section': 'dashboard'})
