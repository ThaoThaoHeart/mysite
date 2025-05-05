from django.urls import path
from . import views
from .views import CustomLoginView, CustomLogoutView, RegisterView, ProtectedView


urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('protected/', ProtectedView.as_view(), name='protected'),
]