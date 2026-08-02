import random
from datetime import timedelta

from django.contrib.auth import logout, login
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import FormView
from datetime import datetime
from account_module.forms import RegisterForm, LoginForm, VerifyRegisterCodeForm, ForgotPasswordForm, ResetPasswordForm, \
    VerifyForgotPasswordCodeForm
from account_module.models import User
from utils.sms import send_verify_sms


# Create your views here.


class RegisterView(FormView):
    template_name = 'account_module/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('verify_register_code')

    def form_valid(self, form):

        username = form.cleaned_data['username']
        phone = form.cleaned_data['phone']
        password = form.cleaned_data['password']


        if User.objects.filter(username__iexact=username).exists():
            form.add_error('username', 'این نام کاربری قبلاً ثبت شده است.')
            return self.form_invalid(form)


        if User.objects.filter(phone=phone).exists():
            form.add_error('phone', 'این شماره موبایل قبلاً ثبت شده است.')
            return self.form_invalid(form)


        self.request.session['register_data'] = {
            'username': username,
            'phone': phone,
            'password': password,
        }

        otp = random.randint(100000, 999999)
        self.request.session['register_otp'] = str(otp)
        self.request.session['register_otp_expire'] = (
                timezone.now() + timedelta(minutes=2)
        ).isoformat()
        print(otp)

        sms_sent = send_verify_sms(phone, otp)

        if not sms_sent:
            form.add_error(
                None,
                'ارسال پیامک تایید با مشکل مواجه شد. لطفاً دوباره تلاش کنید.'
            )
            return self.form_invalid(form)

        return super().form_valid(form)





class VerifyRegisterCodeView(FormView):

    template_name = 'account_module/verify_register_code.html'
    form_class = VerifyRegisterCodeForm
    success_url = reverse_lazy('home')


    def dispatch(self, request, *args, **kwargs):

        if 'register_data' not in request.session:
            return redirect('register')

        return super().dispatch(request, *args, **kwargs)



    def form_valid(self, form):

        user_code = form.cleaned_data['code']

        session_code = self.request.session.get('register_otp')

        expire = self.request.session.get('register_otp_expire')

        if expire is None:

            form.add_error(None, 'کد منقضی شده است.')

            return self.form_invalid(form)

        expire = datetime.fromisoformat(expire)

        if timezone.now() > expire:

            form.add_error(None, 'کد منقضی شده است.')

            return self.form_invalid(form)

        if user_code != session_code:

            form.add_error('code', 'کد وارد شده صحیح نیست.')

            return self.form_invalid(form)

        data = self.request.session.get('register_data')

        user = User(
            username=data['username'],
            phone=data['phone']
        )

        user.set_password(data['password'])

        user.save()

        login(self.request, user)

        del self.request.session['register_data']

        del self.request.session['register_otp']

        del self.request.session['register_otp_expire']

        return super().form_valid(form)


class LoginView(FormView):

    template_name = 'account_module/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):

        username_phone = form.cleaned_data['username_phone']
        password = form.cleaned_data['password']

        user = User.objects.filter(
            Q(username__iexact=username_phone) |
            Q(phone=username_phone)
        ).first()

        if user is None:
            form.add_error(
                'username_phone',
                'نام کاربری یا رمز عبور اشتباه هست '
            )
            return self.form_invalid(form)

        if not user.check_password(password):
            form.add_error(
                'password',
                'نام کاربری یا رمز عبور اشتباه هست'
            )
            return self.form_invalid(form)

        if not user.is_active:
            form.add_error(
                None,
                'حساب کاربری شما فعال نشده است.'
            )
            return self.form_invalid(form)

        remember_me = form.cleaned_data.get("remember_me")

        if remember_me:
            self.request.session.set_expiry(60 * 60 * 24 * 30)  # 30 روز
        else:
            self.request.session.set_expiry(0)  # تا بسته شدن مرورگر

        login(self.request, user)

        return super().form_valid(form)

class ForgotPasswordView(FormView):

    template_name = 'account_module/forgot_password.html'

    form_class = ForgotPasswordForm

    success_url = reverse_lazy('verify_forgot_password')


    def form_valid(self, form):

        phone = form.cleaned_data['phone']


        user = User.objects.filter(phone=phone).first()


        if user is None:

            form.add_error(
                'phone',
                'کاربری با این شماره موبایل وجود ندارد.'
            )

            return self.form_invalid(form)



        otp = random.randint(100000, 999999)


        self.request.session['forgot_password_phone'] = phone

        self.request.session['forgot_password_otp'] = str(otp)


        self.request.session['forgot_password_expire'] = (
            timezone.now() + timedelta(minutes=2)
        ).isoformat()

        print("FORGOT PASSWORD OTP:", otp)

        sms_sent = send_verify_sms(phone, otp)

        if not sms_sent:
            form.add_error(
                None,
                'ارسال پیامک تایید با مشکل مواجه شد. لطفاً دوباره تلاش کنید.'
            )
            return self.form_invalid(form)

        return super().form_valid(form)

class VerifyForgotPasswordCodeView(FormView):

    template_name = 'account_module/verify_forgot_password_code.html'

    form_class = VerifyForgotPasswordCodeForm

    success_url = reverse_lazy('reset_password')


    def dispatch(self, request, *args, **kwargs):

        if 'forgot_password_phone' not in request.session:

            return redirect('forgot_password')


        return super().dispatch(request, *args, **kwargs)



    def form_valid(self, form):

        code = form.cleaned_data['code']

        session_code = self.request.session.get(
            'forgot_password_otp'
        )

        expire = self.request.session.get(
            'forgot_password_expire'
        )

        if expire is None:

            form.add_error(
                None,
                'کد منقضی شده است.'
            )

            return self.form_invalid(form)

        expire = datetime.fromisoformat(expire)

        if timezone.now() > expire:

            form.add_error(
                None,
                'کد منقضی شده است.'
            )

            return self.form_invalid(form)

        if code != session_code:

            form.add_error(
                'code',
                'کد وارد شده صحیح نیست.'
            )

            return self.form_invalid(form)

        return super().form_valid(form)

class ResetPasswordView(FormView):

    template_name = 'account_module/reset_password.html'

    form_class = ResetPasswordForm

    success_url = reverse_lazy('login')


    def dispatch(self, request, *args, **kwargs):

        if 'forgot_password_phone' not in request.session:

            return redirect('forgot_password')


        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):

        phone = self.request.session.get(
            'forgot_password_phone'
        )

        password = form.cleaned_data['password']

        user = User.objects.filter(
            phone=phone
        ).first()

        if user is None:

            form.add_error(
                None,
                'کاربر پیدا نشد.'
            )

            return self.form_invalid(form)

        user.set_password(password)

        user.save()

        self.request.session.pop(
            'forgot_password_phone',
            None
        )

        self.request.session.pop(
            'forgot_password_otp',
            None
        )

        self.request.session.pop(
            'forgot_password_expire',
            None
        )

        return super().form_valid(form)

class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect(reverse('home'))
