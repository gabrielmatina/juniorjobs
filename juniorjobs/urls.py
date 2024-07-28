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
from jobs.views import home, login_view, candidate_register  # Certifique-se de que está importando views corretamente

urlpatterns = [
    path('admin/', admin.site.urls),  # URL padrão para o painel de administração do Django
    path('', home, name='home'),       # URL para a página inicial
    path('login/', login_view, name='login'),  # URL para a página de login
    path('register/', candidate_register, name='candidate_register'),  # URL para o registro de candidatos
]

