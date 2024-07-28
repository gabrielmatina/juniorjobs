from django import forms
from .models import Candidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = [
            'full_name', 'address', 'city', 'state', 'education', 'status',
            'salary_expectation', 'additional_info'
        ]
        widgets = {
            'state': forms.Select(choices=Candidate.STATES),
            'education': forms.Select(choices=Candidate.EDUCATION_CHOICES),
            'status': forms.Select(choices=Candidate.STATUS_CHOICES),
        }
