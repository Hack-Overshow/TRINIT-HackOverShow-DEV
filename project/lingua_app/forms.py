from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TutorLoginForm(AuthenticationForm):
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password:
            user = self.user_cache
            if user is None or user.userprofile.role != 'tutor':
                raise forms.ValidationError('Invalid username or password.')
        return cleaned_data

class StudentLoginForm(AuthenticationForm):
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password:
            user = self.user_cache
            if user is None or user.userprofile.role != 'student':
                raise forms.ValidationError('Invalid username or password.')
        return cleaned_data

class SignupForm(UserCreationForm):
    role = forms.ChoiceField(choices=[('tutor', 'Tutor'), ('student', 'Student')])

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data