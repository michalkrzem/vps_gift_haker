from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from .forms import CreateUserForm
from gifts.models import Invitation


@csrf_exempt
def register_page(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                if Invitation.objects.filter(email=user).exists():
                    invitation_user = Invitation.objects.get(email=user)
                    invitation_user.accepted = True
                    invitation_user.save()

                messages.success(request, "Account was created for " + user)

                return redirect("login")

        context = {"form": form}
        return render(request, "register.html", context)


@csrf_exempt
def login_page(request):
    """
    TODO: Set email as a login field - not username
    TODO: Create AbstractUser, CustomManager, CustomAdminManager
    """
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm(request.POST)
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password1")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Username OR password is incorrect")

        context = {"form": form}
        return render(request, "login.html", context)


@csrf_exempt
def logout_user(request):
    logout(request)
    return redirect("login")
