from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(label="Email",required=True,widget=forms.TextInput(attrs={
        'class':"form-control",
        'placeholder': 'Enter email...' 
    }))

    password = forms.CharField(label="Password",required=True,widget=forms.PasswordInput(attrs={
        'class':"form-control",
        'placeholder': 'Password...'
    }))