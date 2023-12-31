from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'data']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of Article',
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons of Article',
            }),
            'data': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of Publication',
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of Article',
            }),
        }