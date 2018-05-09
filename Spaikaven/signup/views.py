from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('login:login')
    else:
        signup_form = UserCreationForm()
    return render(request, 'signup/signup.html', { 'form': signup_form})
