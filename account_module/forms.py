from django import forms


class RegisterForm(forms.Form):

    username = forms.CharField(
        label='نام کاربری',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام کاربری',
            'id': 'username',
        })
    )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'شماره موبایل',
            'id': 'phone',
            'style': 'direction: rtl; text-align: right;',
        })
    )

    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'رمز عبور',
            'id': 'password',
        })
    )

    password2 = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'تکرار رمز عبور',
            'id': 'password2',
        })
    )

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if len(phone) != 11 or not phone.isdigit():
            raise forms.ValidationError("شماره موبایل معتبر نیست.")

        if not phone.startswith("09"):
            raise forms.ValidationError("شماره باید با 09 شروع شود.")

        return phone

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            self.add_error("password2", "رمزهای عبور یکسان نیستند.")

        return cleaned_data



class LoginForm(forms.Form):
    username_phone = forms.CharField(
        label='نام کاربری یا شماره موبایل',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'username_phone',
                'placeholder': 'نام کاربری یا شماره موبایل',
                'dir': 'rtl',
            }
        ),
        error_messages={
            'required': 'نام کاربری یا شماره موبایل را وارد کنید.'
        }
    )

    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'password',
                'placeholder': 'رمز عبور',
                'dir': 'rtl',
            }
        ),
        error_messages={
            'required': 'رمز عبور را وارد کنید.'
        }
    )
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={

                "id": "remember_me"
            }
        )
    )


class VerifyRegisterCodeForm(forms.Form):
    code = forms.CharField(
        label='',
        max_length=6,
        min_length=6,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'کد تایید',
            'autocomplete': 'off'
        }),
        error_messages={
            'required': 'کد تایید را وارد کنید.',
            'min_length': 'کد باید ۶ رقمی باشد.',
            'max_length': 'کد باید ۶ رقمی باشد.',
        }
    )


class ForgotPasswordForm(forms.Form):

    phone = forms.CharField(
        label='',
        max_length=11,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'شماره موبایل',
            'autocomplete': 'off'
        }),
        error_messages={
            'required': 'شماره موبایل را وارد کنید.',
            'max_length': 'شماره موبایل صحیح نیست.',
        }
    )



class VerifyForgotPasswordCodeForm(forms.Form):

    code = forms.CharField(
        label='',
        max_length=6,
        min_length=6,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'کد تایید',
            'autocomplete': 'off'
        }),
        error_messages={
            'required': 'کد تایید را وارد کنید.',
            'min_length': 'کد باید ۶ رقمی باشد.',
            'max_length': 'کد باید ۶ رقمی باشد.',
        }
    )

class ResetPasswordForm(forms.Form):

    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'رمز عبور جدید',
            'autocomplete': 'new-password'
        }),
        error_messages={
            'required': 'رمز عبور جدید را وارد کنید.',
        }
    )


    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'تکرار رمز عبور جدید',
            'autocomplete': 'new-password'
        }),
        error_messages={
            'required': 'تکرار رمز عبور را وارد کنید.',
        }
    )


    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')


        if password and password2 and password != password2:
            self.add_error(
                'password2',
                'رمزهای عبور یکسان نیستند.'
            )

        return cleaned_data