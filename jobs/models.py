from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class MyModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('candidate', 'Candidate'),
        ('company', 'Company'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

class Job(models.Model):
    SALARY_CHOICES = [
        ('0-1000', 'Até 1.000'),
        ('1000-2000', 'De 1.000 a 2.000'),
        ('2000-3000', 'De 2.000 a 3.000'),
        ('3000+', 'Acima de 3.000')
    ]
    EDUCATION_CHOICES = [
        ('fundamental', 'Ensino Fundamental'),
        ('medio', 'Ensino Médio'),
        ('tecnologo', 'Tecnólogo'),
        ('superior', 'Ensino Superior'),
        ('mba', 'Pós / MBA / Mestrado'),
        ('doutorado', 'Doutorado')
    ]
    name = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=20, choices=SALARY_CHOICES)
    requirements = models.TextField()
    minimum_education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    company = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='jobs')

class Candidate(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    education = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    salary_expectation = models.DecimalField(max_digits=10, decimal_places=2)
    additional_info = models.TextField()

    def __str__(self):
        return self.full_name

class Application(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interviewed', 'Interviewed'),
        ('hired', 'Hired'),
        ('rejected', 'Rejected')
    ]
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')

    def __str__(self):
        return f"{self.candidate.full_name} applied for {self.job.name}"
