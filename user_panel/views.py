from django.views.generic import TemplateView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ChangePasswordForm


# Create your views here.



class TrackingView(TemplateView):
    template_name = 'user_panel/tracking.html'



class ChangePasswordView(LoginRequiredMixin, FormView):

    template_name = 'user_panel/change_password.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('home')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs['user'] = self.request.user

        return kwargs


    def form_valid(self, form):

        user = self.request.user

        user.set_password(
            form.cleaned_data['password']
        )

        user.save()

        #کاربر بعد از تغییر رمز بیرون نمیپره و سشن اپدیت میشه
        update_session_auth_hash(
            self.request,
            user
        )


        return super().form_valid(form)