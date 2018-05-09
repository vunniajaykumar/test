from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()    # user()-> variable
            login(request, user)
            if'next'in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home:home')
    else:
        login_form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': login_form})

def logout_view(required):
    logout(required)
    return redirect('login:login')
