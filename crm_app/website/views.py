from django.contrib import messages  # for flash messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import AddRecordForm, SignUpForm
from .models import Record

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            #authenticate and log in
            username = form.cleaned_data['username']
            #email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been registered")
                return redirect('home')
            else:
                messages.error(request, "Authentication failed")
                return redirect('register')
    else:
        form = SignUpForm()
        
    
    return render(request, 'register.html', {'form': form})


def home(request):
    records = Record.objects.all()
    
    
    
    
    #check if user is login in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.error(request, "There was an error")
            return redirect('home')
     
    else:
        return render(request, 'home.html', {'records' : records})





def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


def customer_record(request, pk):
    if request.user.is_authenticated:
        #look up a record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.error(request, "You must be logged in to view this page")
        return redirect('home')

  
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record) #adds stuff to the form
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been Updated")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to view this page")
    return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        rec_delete = Record.objects.get(id=pk)
        rec_delete.delete()
        messages.success(request, "Record deleted successfully")
        return redirect('home')
    else:
        messages.error(request, "You must be logged in to view this page")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added Successfully")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to view this page")
        return redirect('home')