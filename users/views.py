from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView

from users.models import User
from .tokens import TokenGenerator
from azshop.settings import EMAIL_HOST_USER


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
            return redirect('registration')
        if User.objects.filter(email=email).exists():
            messages.error(request, "User with this email already exists.")
            return redirect('registration')
        if User.objects.filter(phone=phone).exists():
            messages.error(request, "User with this phone number already exists.")
            return redirect('registration')
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=pass_1,
            phone=phone,
            username=phone,
        )
        user.is_active = False
        user.save()

         # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ AZ"
        message = render_to_string('email_confirmation.html',{
            'name': user.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': TokenGenerator().make_token(user)
        })
        email = EmailMessage(
            email_subject,
            message,
            EMAIL_HOST_USER,
            [user.email],
        )
        send_mail(email_subject, message, EMAIL_HOST_USER, user.email, fail_silently=True)
        return redirect('signin')
    

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
            return redirect('signin')
        return render(request, 'activation_failed.html')