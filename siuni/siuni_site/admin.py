from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Usuario, Disciplina, Turma, Aluno, Professor, Avaliacao, Nota, Falta, MediaFinal, Noticia, Post])