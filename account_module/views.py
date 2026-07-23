from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class RegisterView(TemplateView):

    template_name = 'account_module/register.html'




class LoginView(TemplateView):

    template_name = 'account_module/login.html'
