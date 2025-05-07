from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class HomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        return render(request, 'auth1_app/home.html')

class CustomLoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class RegisterView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect('home')

class ProtectedView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'registration/protected.html')
        else:
            return redirect('login')





































# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.decorators import login_required
# from django.views.generic import CreateView, TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import UserRegistrationForm
# from django.urls import reverse_lazy

# class HomeView(LoginRequiredMixin, TemplateView):
#     template_name = 'auth1_app/home.html'

# class CustomLoginView(LoginView):
#     template_name = 'accounts/login.html'

# class CustomLogoutView(LogoutView):
#     next_page = reverse_lazy('login')

# class RegisterView(CreateView):
#     form_class = UserRegistrationForm
#     template_name = 'accounts/register.html'
#     success_url = reverse_lazy('home')  

#     def form_valid(self, form):
#         # Save the user
#         response = super().form_valid(form)
#         # Log in the user
#         user = form.instance
#         login(self.request, user)
#         return response

# class ProtectedView(LoginRequiredMixin, TemplateView):
#     template_name = 'registration/protected.html'
#     login_url = reverse_lazy('login')