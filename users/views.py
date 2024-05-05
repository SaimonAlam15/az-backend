from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from .models import User, AddressBook
from .tokens import TokenGenerator
from azshop.settings import EMAIL_HOST_USER
from .serializers import UserSerializer, AddressBookSerializer



def send_confirmation_email(request, user):
    current_site = get_current_site(request)
    email_subject = "Confirm your Email @ AZ"
    message = render_to_string('email_confirmation.html',{
            'name': user.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': TokenGenerator().make_token(user)
        })
    send_mail(
            email_subject, message, EMAIL_HOST_USER,
            [user.email], fail_silently=False
    )


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        pass_1 = data.get("pass_1")
        pass_2 = data.get("pass_2")
        phone = data.get("phone")
        if pass_1 != pass_2:
            messages.error(request, "Passwords do not match.")
            return Response(status=400, data={"error": "Passwords do not match."})
        if User.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists.")
            return Response(status=400, data={"error": "User with this email already exists."})
        if User.objects.filter(phone=phone).exists():
            messages.error(request, "User with this phone number already exists.")
            return Response(status=400, data={"error": "User with this phone number already exists."})
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=pass_1,
            phone=phone,
            username=email,
        )
        user.is_active = False

        try:
            # Email Address Confirmation Email
            send_confirmation_email(request, user)
            user.save()
        except Exception as e:
            messages.error(request, str(e))
            return Response(status=400, data={"error": str(e)})
        return Response(status=201, data={"message": "User created successfully."})


class ActivationView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception:
            user = None
        if user is not None and TokenGenerator().check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Account activated successfully.")
            return render(request, "login.html", status=200)
        return render(request, 'confirmation_failed.html', status=400)


class LoginView(APIView):
    def post(self, request):
        data = request.data
        email = data.get("email")
        password = data.get("password")

        user = authenticate(username=email, password=password)
        refresh = RefreshToken.for_user(user)
        if user is not None:
            login(request, user)
            return Response(status=200, data={
                "message": "User logged in successfully.",
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            })
        return Response(status=400, data={"error": "Invalid email or password."})

class LogoutView(APIView):
    def get(self, request):
        logout(request)
        messages.success(request, "Logged out successfully!")
        return redirect("")


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if 'email' in request.data:
            request.data['is_active'] = False
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if 'email' in request.data:
        # Send email confirmation email
            try:
                send_confirmation_email(request, self.get_object())
                logout(request)
                return redirect("")
            except Exception as e:
                return Response(status=400, data={"error": str(e)})
        return Response(serializer.data)

class AddressBookListView(ListCreateAPIView):
    serializer_class = AddressBookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return AddressBook.objects.filter(user=self.kwargs.get("user_id"))

    def perform_create(self, serializer):
        user = User.objects.get(pk=self.kwargs.get("user_id"))
        serializer.save(user=user)


class AddressBookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = AddressBook.objects.all()
    serializer_class = AddressBookSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "address_id"

    def get_queryset(self):
        return AddressBook.objects.filter(user=self.kwargs.get("user_id"))