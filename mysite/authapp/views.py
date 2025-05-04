from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            new_user = User.objects.create_user(
                username=username,
                password=password,
            )
            login(request, new_user)
            return redirect('account')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    error_message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            error_message = 'Invalid credentials'
    return render(request, 'accounts/login.html', {'error': error_message})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('account')
    
@login_required
def home(request):
    return render(request, 'auth1_app/home.html')

# Protected View (Mimic - Only restricted to login users)
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    
    def get(self, request):
        return render(request, 'registration/protected.html')
