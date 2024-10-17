from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Usuario, Aluno, Professor, SituacaoAcademica, Nota, Avaliacao, Falta, MediaFinal, Disciplina, Turma])