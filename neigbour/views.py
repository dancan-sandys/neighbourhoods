from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import user, Business, neighbourhood


def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(loginpage)

    return render(request,'accounts/signup.html',{"form":form})


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'accounts/login.html')

def logoutuser(request):
    logout(request)
    return redirect(loginpage)

def home(request):

    return render(request, 'home.html')

def myneigbourhood(request):
    User = request.user
    User = user.objects.get(user = User)
    Neighbourhood = User.Neighbourhood

    return render(request, 'myneigbourhood.html',{"user":User, "myneighbourhood":Neighbourhood})

def profile(request):
    User = request.user
    User = user.objects.get(user = User)

    return render(request, 'profile.html',{"account":User })


def allneighbourhoods(request):
    neighbourhoods = neighbourhood.objects.all()

    return render(request, 'allneighbourhoods.html',{"neigbourhoods":neighbourhoods})

def businesses(request):
    allbusinesses = Business.objects.all()

    return render(request, 'businesses.html',{"businesses":allbusinesses})