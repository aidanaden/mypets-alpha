from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import MyPetsLoginForm, MyPetsRegisterForm


def login(request):
    print('login requested')
    if request.method == "POST":
        print(request.POST.get('formtype'))
        if request.POST.get('formtype') == 'login':
            f = MyPetsLoginForm(request.POST)
            if f.is_valid():
                username = f.cleaned_data.get('username')
                password = f.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('store-home')
                else:
                    print("LOGIN FAILED!")
                    return redirect('login')

        elif request.POST.get('formtype') == 'register':
            f = MyPetsRegisterForm(request.POST)
            if f.is_valid():
                f.save()
                return redirect('store-home')
    else:
        print('HELLO')
        return render(request, template_name='users/login.html')
