from django import forms
from .models import ProductComment


class ProductCommentForm(forms.ModelForm):

    class Meta:
        model = ProductComment
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'نظر خود را بنویسید'
            })
        }