from django.shortcuts import render , redirect
from .forms import RegistrationForm
from .models import Account , Email_history , Email_passwords
from django.contrib import messages , auth
from django.contrib.auth.decorators import login_required



# ========= register =========
def register (request):
    if request.method == 'POST':
        form  = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = Account.objects.create_user(first_name = first_name , last_name = last_name , email = email ,username =username , password = password)
            user.save()
            email_password_account = Email_passwords(user = user,)
            email_password_account.save()
            messages.success(request , 'Successfully registred')
            return redirect ('register')
    else:
        form = RegistrationForm()
    context = {
        'form' : form
    }

    return render(request , 'users/register.html' , context)

# ========= login =========
def login (request):
    if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            
            user = auth.authenticate(email = email , password = password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.error(request , 'Invalid login credentials!')
                return redirect('login')
    return render(request , 'users/login.html')

# ========= logout =========
@login_required(login_url='login')
def logout (request):
    auth.logout(request)
    messages.success(request , 'You are logged out!')
    return redirect('login')

# ========= reset password =========
def reset_password(request):
    return render(request, 'users/reset-password.html')

# ========= account =========
@login_required(login_url='login')
def account(request):
        try:
            email_history = Email_history.objects.filter(user = request.user)
            email_password = Email_passwords.objects.get(user = request.user)
            context ={
                "email_history":email_history,
                "email_password":email_password,
            }
        except:
            pass
        return render(request, 'users/account.html' , context)


def update_info(request):
        try:
            if request.method == 'POST':
                    first_name = request.POST['first_name']
                    last_name = request.POST['last_name']
                    username = request.POST['username']
                    account = Account.objects.get(email = request.user)
                    account.first_name = first_name
                    account.last_name = last_name
                    account.username = username # this we should check if already exist another username the same
                    account.save()
                    #email_passwords
                    email_passwords = Email_passwords.objects.get(user = request.user)
                    email_password = request.POST['password']
                    email_password_confirm = request.POST['confirm_password']
                    
                    if len(email_password) == 0 or len(email_password_confirm) == 0:
                        messages.error(request, 'Please put your email password.')
                    elif email_password == email_password_confirm:
                        email_passwords.password = email_password
                        email_passwords.save()
                        messages.success(request , 'Your informations have been successfully changed.')
                    else:
                        messages.error(request , 'Password does not match!')
                    return redirect('account')    
        except:
            pass