from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import Utilisateur
from django.contrib.auth import authenticate, login
from django.contrib import messages

def inscription(request):
    form2 = Utilisateur()
    if request.method=='POST':
        form2 = Utilisateur(request.POST)
        if form2.is_valid():
            form2.save()
            user=form2.cleaned_data.get('username')
            messages.success(request, 'Your account is Successful create pour '+user)
            return redirect('acces')
    context={'form2': form2}
    return render(request, 'inscription.html', context)

def acces(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(password)
        user=authenticate(request, username=username,password= password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Some error in Username and/or Password")
    return render(request, 'acces.html', { })

