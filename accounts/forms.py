from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(label="Email",required=True,widget=forms.TextInput(attrs={
        'class':"min-w-full border rounded px-2 py-1 border-orange-300 focus-within:outline-orange-500",
        'placeholder': 'Enter email...' 
    }))

    password = forms.CharField(label="Password",required=True,widget=forms.PasswordInput(attrs={
        'class':"min-w-full border rounded px-2 py-1 border-orange-300 focus-within:outline-orange-500",
        'placeholder': 'Password...'
    }))