from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test


def redirect_if_authenticated(user):
    return not user.is_authenticated

# home page
@user_passes_test(redirect_if_authenticated, login_url='dashboard')  # Redirect to the home page
def home(request):
    return render(request, 'app/index.html')

# register page
@user_passes_test(redirect_if_authenticated, login_url='dashboard')  # Redirect to the home page
def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    context = {'form':form}
    return render(request, 'app/register.html', context=context)

@user_passes_test(redirect_if_authenticated, login_url='dashboard')  # Redirect to the home page
def login(request):
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'form':form}

    return render(request, 'app/login.html', context=context)


def logout(request):

    auth.logout(request)
    return redirect("login")

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'app/dashboard.html')


