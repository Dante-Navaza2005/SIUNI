from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Documento, Usuario, Aluno, Professor, SituacaoAcademica])