from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    RegistrationView, ActivationView, LoginView, LogoutView, UserListView,
    UserDetailView, AddressBookListView, AddressBookDetailView
)

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('activate/<uidb64>/<token>', ActivationView.as_view(), name='activate'),
    path('signup', RegistrationView.as_view(), name='registration'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path(
        'password-reset/', PasswordResetView.as_view(
            template_name='password_reset.html'), name='password_reset'
    ),
    path(
        'password-reset-done', PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'), name='password_reset_done'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html'), name='password_reset_confirm'
    ),
    path(
        'password-reset-complete', PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'), name='password_reset_complete'
    ),
    path(
        '<int:user_id>/address-book/', AddressBookListView.as_view(),
        name='address_book_list'
    ),
    path(
        '<int:user_id>/address-book/<int:address_id>', AddressBookDetailView.as_view(),
        name='address_book_detail'
    ),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]