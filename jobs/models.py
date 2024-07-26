from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_company = models.BooleanField(default=False)

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
