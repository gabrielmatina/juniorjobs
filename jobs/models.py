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

class Candidate(models.Model):
    EDUCATION_CHOICES = [
        ('Fundamental', 'Ensino fundamental'),
        ('Medio', 'Ensino médio'),
        ('Tecnologo', 'Tecnólogo'),
        ('Superior', 'Ensino Superior'),
        ('Pos', 'Pós'),
        ('MBA', 'MBA'),
        ('Mestrado', 'Mestrado'),
        ('Doutorado', 'Doutorado'),
    ]

    STATUS_CHOICES = [
        ('Estudando', 'Estudando'),
        ('Concluido', 'Concluído'),
        ('Trancado', 'Trancado'),
        ('Interrompido', 'Interrompido'),
    ]

    STATES = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
        ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
        ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
    ]

    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATES)
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    salary_expectation = models.DecimalField(max_digits=10, decimal_places=2)
    additional_info = models.TextField()

def __str__(self):
    return self.full_name
