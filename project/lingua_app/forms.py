from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Meeting


class MeetingCreateForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ["title_of_meeting", "starting_date_time"]

        widgets = {
            "title_of_meeting": forms.TextInput(attrs={"class": "form-control", "placeholder":
                "Title of the Meeting..."}),
            "starting_date_time": forms.DateTimeInput(attrs={"class": "form-control date"})
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=[('tutor', 'Tutor'), ('student', 'Student')])

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
