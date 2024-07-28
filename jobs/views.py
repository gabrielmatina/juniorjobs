from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .forms import CandidateForm


def home(request):
    return HttpResponse("Bem-vindo ao Junior Jobs!")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'jobs/login.html', {'form': form})

def candidate_register(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CandidateForm()
    return render(request, 'jobs/candidate_register.html', {'form': form})

def available_jobs(request):
    return render(request, 'jobs/available_jobs.html')

def applied_jobs(request):
    return render(request, 'jobs/applied_jobs.html')

def add_job_view(request):
    return render(request, 'jobs/add_job.html')

def view_jobs_view(request):
    return render(request, 'jobs/view_jobs.html')

def reports_view(request):
    return render(request, 'jobs/reports.html')

