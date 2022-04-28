from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from .models import userDetails,searchUser,modelResult
from .forms import Search1, selectChoiceForm, modelResultForm
from django.urls import reverse

# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='main/home.html'
                  )

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})

def search(request):
    form = Search1(request.POST , request.FILES)
    if form.is_valid():
        form.save(commit=True)
        
    else:
        print(form.errors)
    return render(request = request,
                  template_name='main/search.html',
                  context = {"form":form},
                  )

def searchview(request):
    return render(request = request,
                  template_name='main/searchview.html',
                  context = {"search": searchUser.objects.all()})

def selectChoice(request):
    form = selectChoiceForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        
    else:
        print(form.errors)
    return render(request = request,
                  template_name='main/selectChoice.html',
                  context = {"form":form},
                  )

def modelsResultview(request):
    form=modelResultForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request = request,
                  template_name='main/modelResultView.html',
                  context = {"form":form},
                  )

def modelResultSee(request):
        return render(request = request,
                  template_name='main/modelResultForm.html',
                  context = {"search":modelResult.objects.all()})

