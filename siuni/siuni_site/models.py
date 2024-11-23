from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.db.models import UniqueConstraint


TIPO_USUARIO_CHOICES = [
    ('Aluno', 'Aluno'),
    ('Professor', 'Professor'),
]

DIAS_UTEIS_CHOICES = [
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
]

# Create your models here.


class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=200, null = True, blank = True)
    matricula = models.IntegerField(default=0)
    email = models.EmailField(max_length=200, null = True, blank = True)
    telefone = models.IntegerField(default=0)
    user = models.OneToOneField(User, null = True, blank = True, on_delete = models.CASCADE)
    tipo_de_usuario = models.CharField(max_length=200,choices=TIPO_USUARIO_CHOICES)  # Aluno ou Professor
    data_nascimento = models.DateField(null = True, blank = True)

    def __str__(self):
        return f'{self.nome_usuario} - {self.tipo_de_usuario}'


class Disciplina(models.Model):
    codigo_disciplina = models.CharField(max_length=200, null = True, blank = True, unique=True)
    nome_disciplina = models.CharField(max_length=200, null = True, blank = True)
    departamento = models.CharField(max_length=200, null = True, blank = True)
    criterio = models.IntegerField(default=0)
    criterio_formula = models.ImageField(null=True, blank=True)

    
    def __str__(self):
        return f'{self.nome_disciplina} - {self.codigo_disciplina}'


class Professor(models.Model):
    usuario = models.OneToOneField(Usuario, null=True, blank=True,on_delete=models.CASCADE, related_name='professor')
    coordenador = models.BooleanField(default=False)

    def __str__(self):
        return f'Professor {self.usuario.nome_usuario} - Coordenador {self.coordenador}'


class Turma(models.Model):
    codigo_turma = models.CharField(max_length=30, null = True, blank = True, unique=True)
    hora_inicio = models.TimeField(null = True, blank = True)
    hora_fim = models.TimeField(null = True, blank = True)
    dias_semana = MultiSelectField(choices=DIAS_UTEIS_CHOICES, null=True, blank=True)
    disciplina = models.ForeignKey(Disciplina, null=True, blank=True, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=[
                'codigo_turma', 
                'hora_inicio', 
                'hora_fim', 
                'dias_semana', 
                'disciplina', 
                'professor'
            ], name='unique_turma_completa')
        ]

    def __str__(self):
        return f'{self.codigo_turma} - {self.disciplina.nome_disciplina} - {self.dias_semana}'


#? para aluno e professor verificar NO FORMULARIO se realmente sao alunos e professores
class Aluno(models.Model):
    usuario = models.OneToOneField(Usuario, null = True, blank = True,on_delete=models.CASCADE, related_name='aluno')
    numero_periodo = models.IntegerField(default=0, null = True, blank = True)
    creditos_a_cumprir = models.IntegerField(default=0, null = True, blank = True)
    curso = models.CharField(max_length=200, null = True, blank = True)
    turmas = models.ManyToManyField(Turma, blank=True)

    def __str__(self):
        return f'Aluno {self.usuario.nome_usuario}'
    


class Avaliacao(models.Model):
    nome_avaliacao = models.CharField(max_length=200,null = True, blank = True)
    data_avaliacao = models.DateField(null = True, blank = True)
    hora_avaliacao = models.TimeField(null = True, blank = True)
    sala_avaliacao = models.CharField(max_length=200,null = True, blank = True)
    predio_avaliacao = models.CharField(max_length=200,null = True, blank = True)
    peso_avaliacao = models.DecimalField(max_digits=3, decimal_places=1)
    turma = models.ForeignKey(Turma, null=True, blank=True,on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=[
                'nome_avaliacao', 
                'data_avaliacao', 
                'hora_avaliacao', 
                'sala_avaliacao', 
                'predio_avaliacao', 
                'peso_avaliacao', 
                'turma'
            ], name='unique_avaliacao_completa')
        ]
    
    def __str__(self):
        return f'{self.nome_avaliacao} - turma {self.turma.codigo_turma} - Data {self.data_avaliacao} - Predio {self.predio_avaliacao}'




class Nota(models.Model):
    valor = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    avaliacao = models.ForeignKey(Avaliacao,null=True, blank=True,on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno,null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['avaliacao', 'aluno'], name='unique_nota_avaliacao_aluno')
        ]

    def __str__(self):
        return f'Valor nota {self.valor} - Avaliacao {self.avaliacao.nome_avaliacao} - Disciplina {self.avaliacao.turma.disciplina} - Aluno {self.aluno.usuario.nome_usuario}'



class Falta(models.Model):
    total_horas_permitidas = models.IntegerField(default=0,null=True, blank=True)
    total_horas_semestre = models.IntegerField(default=0)
    horas_faltadas = models.IntegerField(default=0)
    aluno = models.ForeignKey(Aluno, null=True, blank=True,on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            UniqueConstraint(fields=['aluno', 'disciplina'], name='unique_falta_aluno_disciplina')
        ]  # Garante que o aluno só possa ter um registro de falta por turma

    def __str__(self):
        return f'Aluno {self.aluno.usuario.nome_usuario} - Disciplina {self.disciplina.nome_disciplina} - Horas faltadas {self.horas_faltadas} - Total horas permitidas {self.total_horas_permitidas}' 



class MediaFinal(models.Model):
    g1 = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    g2 = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    g3 = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    g4 = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    media_final = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    aluno = models.ForeignKey(Aluno, null=True, blank=True,on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            UniqueConstraint(fields=['aluno', 'disciplina'], name='unique_media_aluno_disciplina')
        ]  # Garante que o aluno só possa ter um registro de falta por turma

    def __str__(self):
        return f'Aluno {self.aluno.usuario.nome_usuario} - Disiplina {self.disciplina.nome_disciplina} - Media Final {self.media_final}'


class Noticia(models.Model) :
    titulo = models.CharField(max_length=200, null = True, blank = True)
    autor = models.CharField(max_length=200, null = True, blank = True)
    legenda = models.CharField(max_length=200, null = True, blank = True)
    descricao = models.CharField(max_length=200, null = True, blank = True)

    def __str__(self):
        return f'{self.titulo} - {self.legenda}'
