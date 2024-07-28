from django.urls import path
from .views import home, login_view, candidate_register

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', candidate_register, name='candidate_register'),
]
