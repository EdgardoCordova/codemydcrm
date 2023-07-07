from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

def home(request):
    # Check to see if loggin in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged IN!')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in, please try again....')
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def login_user(request):
    pass
    
def logout_user(request):
    logout(request)
    messages.success(request, "you have been logged out!" )

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            
    return render(request, 'register.html', {})
    
