from django.urls import path
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
        '<int:user_id>/address-book/', AddressBookListView.as_view(),
        name='address_book_list'
    ),
    path(
        '<int:user_id>/address-book/<int:address_id>', AddressBookDetailView.as_view(),
        name='address_book_detail'
    )
]