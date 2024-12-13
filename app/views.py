from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Record
from django.core.paginator import Paginator


def redirect_if_authenticated(user):
    return not user.is_authenticated

# home page
@user_passes_test(redirect_if_authenticated, login_url='dashboard')
def home(request):
    return render(request, 'app/index.html')


# register page
@user_passes_test(redirect_if_authenticated, login_url='dashboard')
def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    context = {'form':form}
    return render(request, 'app/register.html', context=context)


@user_passes_test(redirect_if_authenticated, login_url='dashboard')
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

# dashboard without pagination
# @login_required(login_url='login')
# def dashboard(request):

#     records = Record.objects.all()
#     context = {"records": records}

#     return render(request, 'app/dashboard.html', context=context)


# dashboard with pagination
@login_required(login_url='login')
def dashboard(request):
    # Get all records
    records = Record.objects.all().order_by('-created_at')

    # Set up pagination
    paginator = Paginator(records, 5)  # Show 10 records per page
    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the appropriate page of records

    # Pass the page_obj to the context
    context = {"page_obj": page_obj}
    return render(request, 'app/dashboard.html', context=context)


@login_required(login_url='login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {'form': form}
    return render(request, 'app/create_record.html', context=context)

@login_required(login_url='login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {'form': form}
    return render(request, 'app/update_record.html', context=context)


@login_required(login_url='login')
def view_record(request, pk):

    record = Record.objects.get(id=pk)

    context = {'record': record}
    return render(request, 'app/view_record.html', context=context)



@login_required(login_url='login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    return redirect("dashboard")