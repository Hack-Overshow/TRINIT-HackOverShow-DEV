from django import forms
from django.contrib.auth.forms import AuthenticationForm

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
