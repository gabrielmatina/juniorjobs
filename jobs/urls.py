from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.candidate_register, name='candidate_register'),
    path('available-jobs/', views.available_jobs, name='available_jobs'),
    path('applied-jobs/', views.applied_jobs, name='applied_jobs'),
    path('add-job/', views.add_job_view, name='add_job'),
    path('view-jobs/', views.view_jobs_view, name='view_jobs'),
    path('reports/', views.reports_view, name='reports'),
]
