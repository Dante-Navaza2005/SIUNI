from django.urls import path
from .views import * #? Importing everything from the views folder in the same directory

urlpatterns = [
    path('fazer_login/', fazer_login, name="fazer_login"), 
    path('perfil/', perfil, name="perfil"), 
    path('calendario/', calendario, name="calendario"), 
    path('meuCurso/', meu_curso, name="meu_curso"), 
    path('pucAgora/', puc_agora, name="puc_agora"), 
    path('pucAgora/feed', feed, name="feed"), 
    path('pucAgora/mapa', mapa, name="mapa"), 
    path('pucAgora/siuniMais', siuni_mais, name="siuni_mais"), 

    path('fazerlogout/', fazer_logout, name="fazer_logout"),


    path('modal/<str:modal_name>/', carregar_modal, name='carregar_modal'),
    
    path('', homepage, name="homepage"), #? first parameter is the url, second is what function will be runned at the url, and the third is the internal name of the link used to reference the link regardless of its url domain
]
