from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, editProfileForm
from .models import CustomUser

nickname = "temp"

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username = username, password = password)
            if user is not None:
                login(request, user)   
                return redirect("home")
        return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("home")


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request, "selectLocation.html", {'user':user})
        else:
            return render(request, 'signup.html', {'form' : form})

    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form' : form})

        
def select(request):
    if request.method == "POST":
        user = request.user
        user.lat = request.POST['lat']
        user.lng = request.POST['lng']
        user.save()
        return redirect("home")
    return render(request, "selectLocation.html")

def test(request):
    if request.method == "POST":
        lat = request.POST['lat']
        lng = request.POST['lng']         
    return render(request, "test.html")

def edit_profile(request):
    if request.method == "POST":
        form = editProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect("home") 
    else:
        form = editProfileForm(instance = request.user)
        return render(request, 'edit_profile.html', {'form':form})

