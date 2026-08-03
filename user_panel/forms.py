from django import forms


class ChangePasswordForm(forms.Form):

    old_password = forms.CharField(
        label='رمز عبور فعلی',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'رمز عبور فعلی'
            }
        )
    )

    password = forms.CharField(
        label='رمز عبور جدید',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'رمز عبور جدید'
            }
        )
    )

    password2 = forms.CharField(
        label='تکرار رمز عبور جدید',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'تکرار رمز عبور جدید'
            }
        )
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)


    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')

        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                'رمز عبور فعلی اشتباه است'
            )

        return old_password


    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')


        if password and password2:

            if password != password2:
                self.add_error(
                    'password2',
                    'رمز عبور جدید با تکرار آن مطابقت ندارد'
                )

        return cleaned_data