from django.contrib import admin

from django.contrib import admin
from .models import Candidate, Job, Application

admin.site.register(Candidate)
admin.site.register(Job)
admin.site.register(Application)
