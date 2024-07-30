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
    
    def __init__(self, *args, **kwargs):
        super(CandidateRegisterForm, self).__init__(*args, **kwargs)
        self.fields['state'].empty_label = "Selecione seu estado"
        self.fields['education'].empty_label = "Selecione seu nível de educação"
        self.fields['status'].empty_label = "Selecione seu status"

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

    def __init__(self, *args, **kwargs):
        super(CandidateCreationForm, self).__init__(*args, **kwargs)
        self.fields['state'].empty_label = "Selecione seu estado"
        self.fields['education'].empty_label = "Selecione seu nível de educação"
        self.fields['status'].empty_label = "Selecione seu status"

class JobCreationForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['name', 'salary_range', 'requirements', 'minimum_education', 'company']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['candidate', 'job', 'status']