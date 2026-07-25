from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView


# Create your views here.


class RegisterView(TemplateView):

    template_name = 'account_module/register.html'




class LoginView(TemplateView):

    template_name = 'account_module/login.html'





class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect(reverse('home'))
