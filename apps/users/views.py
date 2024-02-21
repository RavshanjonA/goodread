from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from apps.users.forms import UserRegisterForm, UserLoginForm


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "users/register.html", context={"form": form})

    def post(self, request):
        create_form = UserRegisterForm(request.POST, request.FILES)
        if create_form.is_valid():
            create_form.save()
            return redirect("users:login-page")
        else:
            context = {
                "form": create_form
            }
            return render(request, "users/register.html", context=context)


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "users/login.html", context={"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You have logged in as {username}")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
        else:
            return render(request, "users/login.html", {"form": form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "User successfully loged out")
        return redirect("home")
