from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CandidateRegisterForm, JobForm, CustomUserCreationForm
from .models import Job, Candidate, CustomUser
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages


def home(request):
    return render(request, 'jobs/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if not username or not password:
            return render(request, 'jobs/login.html', {'error': 'Favor digitar seu login e senha'})
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            try:
                candidate = Candidate.objects.get(user=user)
                if candidate.user_type == 'candidate':
                    return redirect('applied_jobs')
                elif candidate.user_type == 'recruiter':
                    return redirect('view_jobs')
            except Candidate.DoesNotExist:
                return redirect('home')
        else:
            return render(request, 'jobs/login.html', {'error': 'Login ou senha inválidos'})
    
    return render(request, 'jobs/login.html')

def candidate_register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        candidate_form = CandidateRegisterForm(request.POST)
        if user_form.is_valid() and candidate_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 'candidate'
            user.save()
            candidate = candidate_form.save(commit=False)
            candidate.user = user
            candidate.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('index')  # Redireciona para a página inicial após o cadastro
    else:
        user_form = CustomUserCreationForm()
        candidate_form = CandidateRegisterForm()
    return render(request, 'jobs/candidate_register.html', {'user_form': user_form, 'candidate_form': candidate_form})

def available_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/available_jobs.html', {'jobs': jobs})

def applied_jobs(request):
    applied_jobs = request.user.candidate.applications.all()
    return render(request, 'jobs/applied_jobs.html', {'applied_jobs': applied_jobs})

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
    jobs = Job.objects.all()
    return render(request, 'jobs/view_jobs.html', {'jobs': jobs})

def reports_view(request):
    return render(request, 'jobs/reports.html')
