from django import forms
from .models import ArticleComment


class ArticleCommentForm(forms.ModelForm):

    class Meta:
        model = ArticleComment
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'متن نظر',
            }),
        }