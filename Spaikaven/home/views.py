from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Message


# Create your views here.
@login_required(login_url='login:login')
def home_view(request):
    message = Message.objects.all().order_by('-date')
    return render (request, 'home/home.html', {'messages': message})

@login_required(login_url='login:login')
def compose_view(request):
    if request.method =='POST':
        form = forms.CreateMessage(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.sender = request.user
            instance.save()
            return redirect('home:home')
    else:
        form = forms.CreateMessage()
    return render (request, 'home/compose.html', {'form': form})


