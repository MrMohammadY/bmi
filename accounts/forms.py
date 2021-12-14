from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db.models import Q

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'google@gmail.com'}),
        }

    def clean_confirm_password(self):
        validate_password(self.cleaned_data['password'])

        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            raise ValidationError('passwords not equal!')
        return self.cleaned_data['confirm_password']


class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Username or Email',
                'class': 'form-control'}
        )
    )

    password = forms.CharField(
        max_length=30,
        min_length=4,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'}
        )
    )

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data['username']
        password = cleaned_data['password']

        user = User.objects.filter(Q(username=username) | Q(email=username)).first()

        if user and user.check_password(password):
            cleaned_data['user'] = authenticate(username=username, password=password)
            return cleaned_data

        raise ValidationError('username or password invalid!')
