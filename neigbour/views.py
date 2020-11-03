from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .models import user, Business, neighbourhood
from .forms import accounts, businessaccount
from django.contrib.auth.decorators import login_required


def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            password = user.password
            return redirect(loginpage)

    return render(request,'accounts/signup.html',{"form":form})


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('profile')

    return render(request, 'accounts/login.html')

def logoutuser(request):
    logout(request)
    return redirect(loginpage)

@login_required(login_url= 'login/')
def home(request):
    User = request.user
    User = user.objects.get(user = User)
    Neighbourhood = User.Neighbourhood


    return render(request, 'home.html', {"user":User, "myneighbourhood":Neighbourhood})

def myneigbourhood(request):
    User = request.user
    User = user.objects.get(user = User)
    Neighbourhood = User.Neighbourhood

    return render(request, 'Neigbourhoods/myneigbourhood.html',{"user":User, "myneighbourhood":Neighbourhood})

def profile(request):
    User = request.user
    try:
        account = user.objects.get(user = User)
        mybusinesses = Business.objects.filter(owner = User)

        return render(request, 'users/profile.html',{"account":account, "businesses": mybusinesses })
    except:
        return redirect(createaccount)


def allneighbourhoods(request):
    neighbourhoods = neighbourhood.objects.all()

    return render(request, 'Neigbourhoods/allneighbourhoods.html',{"neigbourhoods":neighbourhoods})

def businesses(request):
    account = user.objects.get(user = request.user)
    neighbourhoodbusinesses = Business.objects.filter(Neighbourhood = account.Neighbourhood)
    allbusinesses = Business.objects.all()

    return render(request, 'Business/businesses.html',{"businesses":allbusinesses, "ourbusinesses":neighbourhoodbusinesses})


def singlebusiness(request, id):
    business = Business.objects.get(id = id)

    return render(request , 'Business/single.html',{"business": business})

def createaccount(request):
    form =accounts()
    user = request.user
    neighbourhoods = neighbourhood.objects.all()
    if request.method == 'POST':
        form = accounts(request.POST, request.FILES)
        if form.is_valid():
            account = form.save(commit=False)
            selectedneighbourhood = neighbourhood.objects.get(id = int(request.POST['neighbourhood']))
            account.Neighbourhood = selectedneighbourhood
            account.user = user        
            account.save()
        
            return redirect(home)

    return render(request, 'users/createuser.html',{"form":form, "neighbourhoods":neighbourhoods})



def createbusiness(request):
    form = businessaccount()
    neighbourhoods = neighbourhood.objects.all()
    if request.method == 'POST':
        form = businessaccount(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST['neighbourhood'])
            business = form.save(commit=False)
            selectedneighbourhood = neighbourhood.objects.get(id = int(request.POST['neighbourhood']))
            business.Neighbourhood = selectedneighbourhood
            business.owner = request.user
            business.save()

            return redirect('profile')


    return render(request, 'Business/create.html',{"form":form, "neighbourhoods":neighbourhoods})

def searchbusiness(request):
    if 'category' in request.GET and request.GET['category']:
        searchedcategory = request.GET.get("category")
        searchresults = Business.searchbusiness(searchedcategory)
        if searchresults:
            return render(request,'search.html', {"results":searchresults})

        else:
            message = "Sorry! The category you entered is not yet available"

            return render(request,'search.html',{"message":message})   

    else:
        message = "Sorry! The category you entered is not yet available"

        return render(request,'search.html',{"message":message})        

