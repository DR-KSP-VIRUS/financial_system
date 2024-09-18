from django import forms
from django.db import transaction

from . import models as mdl


class LoginForm(forms.Form):
    email = forms.CharField(label="Email",required=True,widget=forms.TextInput(attrs={
        'class':"form-control",
        'placeholder': 'Enter email...' 
    }))

    password = forms.CharField(label="Password",required=True,widget=forms.PasswordInput(attrs={
        'class':"form-control",
        'placeholder': 'Password...'
    }))

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(label='password',max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'class':"form-control",
        'placeholder':'Enter at least 6 unique characters'
    }))

    password2 = forms.CharField(label='Confirm Password', max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'class':"form-control",
        'placeholder':"Confirm password"
    }))
    class Meta:
        model = mdl.User
        fields = ('full_name', 'email','phone')

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':"e.g Konja Kuma Sampson"
            }),
            'email': forms.EmailInput(attrs={
                'class':"form-control",
                'placeholder':"Enter active email"
            }),
            'phone': forms.TextInput({
                'class':"form-control",
                'placeholder': 'Your Phone Number'
            }),
        }

    def cleaned_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if(password1 and password2) and (password2 == password1):
            return password2
        raise forms.ValidationError('Passwords do not match')
    
    @transaction.atomic
    def save(self, commit: bool = False):
        user = super().save(commit)
        user.email = self.cleaned_data.get('email')
        user.full_name = self.cleaned_data.get('full_name')
        user.set_password(self.cleaned_password())
        user.customer = True
        user.save()
        return user