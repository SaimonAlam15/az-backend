from django.urls import path
from .views import RegistrationView, ActivationView, LoginView, LogoutView

urlpatterns = [
    path('activate/<uidb64>/<token>', ActivationView.as_view(), name='activate'),
    path('signup', RegistrationView.as_view(), name='registration'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]