from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, PhoneForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        login(request, new_user)
        return redirect("home")

    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("home")

def contact_view(request):
    form = PhoneForm(request.POST or None)
    if form.is_valid():
        phone = form.cleaned_data.get("phone")
    context = {
        "form": form,
    }
    return render(request, "contact.html", context)

