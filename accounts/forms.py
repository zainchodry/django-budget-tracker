from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label = 'Full Name', widget = forms.TextInput(attrs = {'class':'form-control'}))
    email = forms.EmailField(label = 'Email', widget = forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs = {'class':'form-control'}))
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput(attrs = {'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']





class LoginForm(AuthenticationForm):
    username = forms.CharField(label = 'Email', widget = forms.EmailInput(attrs = {'class':'form-control'}))
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs = {'class':'form-control'}))

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        try:
            user = User.objects.get(email = email)
            self.cleaned_data['username'] = user.username

        except:
            raise forms.ValidationError("Invalid Email or Password")
        
        return super().clean()
