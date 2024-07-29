from django import forms
from .models import Candidate, Job, CustomUser, Application
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CandidateRegisterForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [
            'full_name', 'address', 'city', 'state', 'education',
            'status', 'salary_expectation', 'additional_info'
        ]

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['name', 'salary_range', 'requirements', 'minimum_education']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type')

class CandidateCreationForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ('full_name', 'address', 'city', 'state', 'education', 'status', 'salary_expectation', 'additional_info')

class JobCreationForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['name', 'salary_range', 'requirements', 'minimum_education', 'company']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['candidate', 'job', 'status']