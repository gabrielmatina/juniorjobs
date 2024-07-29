from django import forms
from .models import Candidate, Job

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
