# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from myapp.models import TblUser
from .forms import UserForm
from django.contrib.auth import logout

# Logout function
def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Manually authenticate the user from the TblUser model
            user = TblUser.objects.get(username=username, password=password)  # No hash comparison
            # Set session data manually
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('success_page')  # Redirect to the success page
        except TblUser.DoesNotExist:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

# Read - Display all users
def user_list(request):
    users = TblUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

# Create - Add a new user
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

# Update - Edit an existing user
def user_update(request, id):
    user = get_object_or_404(TblUser, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

def user_detail(request, id):
    user = get_object_or_404(TblUser, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_detail.html', {'form': form})

# Delete - Remove a user
def user_delete(request, id):
    user = get_object_or_404(TblUser, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})

def accounting(request):
    return render(request, 'accounting.html')

def report_view(request):
    return render(request, 'report.html')

def vendor_view(request):
    return render(request, 'vendor.html')

def customer_view(request):
    return render(request, 'customer.html')

def ledger_view(request):
    return render(request, 'ledger.html')