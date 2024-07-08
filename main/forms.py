from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator, MaxLengthValidator
from django_recaptcha.fields import ReCaptchaField
from .models import Payment, Connect


class UserCreation(UserCreationForm):
    # captcha = ReCaptchaField()
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password 1'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password 2'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', ]


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'password1']


class PaymentForm(forms.Form):
    card_number = forms.CharField(
        validators=[MinLengthValidator(16)],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Номер карты'
            }
        )
    )
    cvc = forms.IntegerField(
        validators=[MaxLengthValidator(3)],
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'CVC'
            }
        )
    )
    price = forms.FloatField(
        validators=[MinValueValidator(1)],
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Price'
            }
        )
    )

    class Meta:
        model = Payment
        fields = ['card_number', 'cvc', 'price']

    def save(self, commit=True):
        payment = super().save(commit=False)
        if commit:
            payment.save()
        return payment


class ConnectForm(forms.Form):
    quantity = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Кол-во'
            }
        )
    )

    class Meta:
        model = Connect
        fields = ['quantity']
