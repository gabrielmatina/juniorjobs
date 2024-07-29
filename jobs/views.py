from django.shortcuts import render, redirect
from .forms import CandidateRegisterForm, JobForm
from .models import Job, Candidate

def home(request):
    return render(request, 'jobs/home.html')

def login_view(request):
    return render(request, 'jobs/login.html')

def candidate_register(request):
    if request.method == 'POST':
        form = CandidateRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CandidateRegisterForm()
    return render(request, 'jobs/candidate_register.html', {'form': form})

def available_jobs(request):
    return render(request, 'jobs/available_jobs.html')

def applied_jobs(request):
    return render(request, 'jobs/applied_jobs.html')

def add_job_view(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobForm()
    return render(request, 'jobs/add_job.html', {'form': form})

def view_jobs_view(request):
    return render(request, 'jobs/view_jobs.html')

def reports_view(request):
    return render(request, 'jobs/reports.html')
