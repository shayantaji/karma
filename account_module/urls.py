from django.urls import path
from . import  views

urlpatterns = [

    path('login/', views.LoginView.as_view(), name='login'),

    path('register/', views.RegisterView.as_view(), name='register'),

    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('verify-register-code/',views.VerifyRegisterCodeView.as_view(),name='verify_register_code'),

    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot_password'),

    path( 'verify-forgot-password/', views.VerifyForgotPasswordCodeView.as_view(), name='verify_forgot_password'),

    path('reset-password/', views.ResetPasswordView.as_view(), name='reset_password'),

]