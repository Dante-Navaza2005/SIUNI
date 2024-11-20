from django.urls import path
from .views import * #? Importing everything from the views folder in the same directory

urlpatterns = [
    path('fazer_login/', fazer_login, name="fazer_login"), 
    path('perfil/', perfil, name="perfil"), 
    path('calendario/', calendario, name="calendario"), 
    path('meu_curso/', meu_curso, name="meu_curso"), 
    path('puc_agora/', puc_agora, name="puc_agora"), 
    path('', homepage, name="homepage"), #? first parameter is the url, second is what function will be runned at the url, and the third is the internal name of the link used to reference the link regardless of its url domain
]
