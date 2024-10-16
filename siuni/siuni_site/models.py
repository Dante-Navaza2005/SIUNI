from django.db import models
from django.contrib.auth.models import User

TIPO_USUARIO_CHOICES = [
    ('Aluno', 'Aluno'),
    ('Professor', 'Professor'),
]


# Create your models here.
class Documento(models.Model):
    nome_documento = models.CharField(max_length=200, null=True, blank=True)
    data_nascimento = models.CharField(max_length=200, null = True, blank = True)
    cpf = models.CharField(max_length=200, null = True, blank = True)
    rg = models.CharField(max_length=200, null = True, blank = True)
    
    def __str__(self):
        return f'{self.nome_documento}'

class Usuario(models.Model):
    nome = models.CharField(max_length=200, null = True, blank = True)
    email = models.CharField(max_length=200, null = True, blank = True)
    telefone = models.CharField(max_length=200, null = True, blank = True)
    user = models.OneToOneField(User, null = True, blank = True, on_delete = models.CASCADE)
    documento = models.OneToOneField(Documento, null = True, blank = True, on_delete = models.CASCADE)
    tipo_de_usuario = models.CharField(max_length=50, choices=TIPO_USUARIO_CHOICES)  # Aluno ou Professor

    def __str__(self):
        return f'{self.nome} - {self.tipo_de_usuario}'


#? para aluno e professor verificar NO FORMULARIO se realmente sao alunos e professores
class Aluno(models.Model):
    matricula = models.CharField(max_length=7, primary_key=True)  # Matricula PK
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='aluno')

    def __str__(self):
        return f'Aluno {self.usuario.nome}'
    

class Professor(models.Model):
    matricula = models.CharField(max_length=7, primary_key=True)  # Matricula PK
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='professor')
    coordenador = models.BooleanField(default=False)

    def __str__(self):
        return f'Professor {self.usuario.nome} - Coordenador {self.coordenador}'



#oi