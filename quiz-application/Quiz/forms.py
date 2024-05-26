from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import QuesModel

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email','password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['first_name'].label = 'First Name'
        self.fields['last_name'].label = 'Last Name'
        self.fields['email'].label = 'Email'
        self.fields['password1'].help_text = "Your password must contain at least 8 characters, can't be too similar to your other personal information, can't be a commonly used password, and can't be entirely numeric."
        self.fields['password2'].label = 'Confirm Password'
        self.fields['username'].help_text = ""  # Set help text to empty string
       


class addQuestionform(forms.ModelForm):
    class Meta:
        model = QuesModel
        fields = ['category', 'question', 'option1', 'option2', 'option3', 'option4', 'answer']
        widgets = {
            'category': forms.Select(choices=QuesModel.CATEGORY_CHOICES, attrs={'class': 'form-control'}),
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'option1': forms.TextInput(attrs={'class': 'form-control'}),
            'option2': forms.TextInput(attrs={'class': 'form-control'}),
            'option3': forms.TextInput(attrs={'class': 'form-control'}),
            'option4': forms.TextInput(attrs={'class': 'form-control'}),
            'answer': forms.Select(choices=QuesModel.OPTION_CHOICES, attrs={'class': 'form-control'}),
        }