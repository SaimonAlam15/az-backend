from django.urls import path
from .views import RegistrationView, ActivationView

urlpatterns = [
    path('activate/<uidb64>/<token>/', ActivationView.as_view(), name='activate'),
    path('signup/', RegistrationView.as_view(), name='registration'),
]