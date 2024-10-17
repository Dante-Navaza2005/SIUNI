from django.db import models
from django.contrib.auth.models import User

TIPO_USUARIO_CHOICES = [
    ('Aluno', 'Aluno'),
    ('Professor', 'Professor'),
]


# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=200, null = True, blank = True)
    email = models.CharField(max_length=200, null = True, blank = True)
    telefone = models.CharField(max_length=200, null = True, blank = True)
    user = models.OneToOneField(User, null = True, blank = True, on_delete = models.CASCADE)
    tipo_de_usuario = models.CharField(max_length=50, choices=TIPO_USUARIO_CHOICES)  # Aluno ou Professor

    def __str__(self):
        return f'{self.nome} - {self.tipo_de_usuario}'


class SituacaoAcademica(models.Model):
    nPerido = models.IntegerField(default=0)
    creditos = models.IntegerField(default=0)
    codCurso = models.CharField(max_length=200, null=True, blank=True) #depois vincular com tabela curso

    def __str__(self):
        return f'nPeriodo {self.nPerido} - creditos {self.creditos}'


#? para aluno e professor verificar NO FORMULARIO se realmente sao alunos e professores
class Aluno(models.Model):
    matricula = models.CharField(max_length=7, primary_key=True)  # Matricula PK
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='aluno')
    situacao_academica = models.OneToOneField(SituacaoAcademica, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Aluno {self.usuario.nome}'
    

class Professor(models.Model):
    matricula = models.CharField(max_length=7, primary_key=True)  # Matricula PK
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='professor')
    coordenador = models.BooleanField(default=False)

    def __str__(self):
        return f'Professor {self.usuario.nome} - Coordenador {self.coordenador}'
    
class Nota(models.Model):
    numAvaliacao = models.IntegerField(default=0)
    valor = models.IntegerField(default=0)

    # def __str__(self):
    #     return f'{Nota} - {valor}'


class Avaliacao(models.Model):
    data = models.DateField(null = True)
    horas = models.TimeField(null = True, blank = True)
    nSala = models.IntegerField(default=0)
    predio = models.CharField(max_length=2, primary_key= True)
    peso = models.IntegerField(default=0)


    # def __str__(self):
    #     return f'{nSala} - {data}'


class Falta(models.Model):
    totFaltasPerm = models.IntegerField(default=0)
    totHorasSemestre = models.IntegerField(default=0)
    horasFaltadas = models.IntegerField(default=0)



class MediaFinal(models.Model):
    g1 = models.DecimalField(default=0)
    g2 = models.DecimalField(default=0)
    g3 = models.DecimalField(default=0)
    g4 = models.DecimalField(default=0)
    mediaFinal = models.DecimalField(default=0)

class Disciplina(models.Model):
    codDisciplina = models.CharField(max_length=12, primary_key= True)
    nomeDisciplina = models.CharField(max_length=100, primary_key= True)
    critero = models.IntegerChoices(default=0)
    departamento = models.CharField(max_length=100, primary_key= True)



class Turma(models.Model):
    horas = models.TimeField(null = True, blank = True)
    data = models.DateField(null=True)
    codTurma = models.CharField(max_length=30, primary_key=True)