from django.contrib import admin
from .models import CustomUser, Job, Candidate, Application
from .forms import JobCreationForm, ApplicationForm, CustomUserCreationForm, CandidateCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type',)}),
    )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:  # Novo usuário
            if obj.user_type == 'candidate':
                Candidate.objects.create(user=obj)

admin.site.register(CustomUser, CustomUserAdmin)

class CandidateAdmin(admin.ModelAdmin):
    form = CandidateCreationForm

admin.site.register(Candidate, CandidateAdmin)

class JobAdmin(admin.ModelAdmin):
    form = JobCreationForm

admin.site.register(Job, JobAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    form = ApplicationForm
    list_display = ['candidate', 'job', 'status']
    search_fields = ['candidate__full_name', 'job__name']
    list_filter = ['status']

admin.site.register(Application, ApplicationAdmin)
