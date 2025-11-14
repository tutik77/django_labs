from django import forms
from .models import Feedback, Subscriber


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема сообщения'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше сообщение...',
                'rows': 5
            }),
        }
        labels = {
            'name': 'Ваше имя',
            'email': 'Email адрес',
            'subject': 'Тема сообщения',
            'message': 'Сообщение'
        }

class SubscriptionForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ваш email'
    }), label='Email')

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        if Subscriber.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError('Вы уже подписаны')
        return email

class UnsubscribeForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ваш email'
    }), label='Email')

