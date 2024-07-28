"""
URL configuration for juniorjobs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jobs.views import home, login_view, candidate_register, available_jobs, applied_jobs, add_job_view, view_jobs_view, reports_view

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', home, name='home'),      
    path('login/', login_view, name='login'),  
    path('register/', candidate_register, name='candidate_register'),  
    path('available-jobs/', available_jobs, name='available_jobs'),
    path('applied-jobs/', applied_jobs, name='applied_jobs'),
    path('add-job/', add_job_view, name='add_job'),
    path('view-jobs/', view_jobs_view, name='view_jobs'),
    path('reports/', reports_view, name='reports'),
]

