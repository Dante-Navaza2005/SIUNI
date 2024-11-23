from django.shortcuts import render, redirect
from .models import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.common.exceptions import NoSuchElementException, WebDriverException

from django.http import HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



from .utils import *

def fazer_login(request):
    error = None
    context = {}

    #! FAZENDO O LOGIN
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        senha = request.POST.get('senha')

        user = authenticate(username=matricula, password=senha)

        if not user :
            # Configuração do Selenium para login automático
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-gpu")

            try:
                # Inicia o ChromeDriver automaticamente usando webdriver-manager
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

                preencher_login(driver, matricula, senha)
                

                # Verificar se o login foi bem-sucedido
                page_content = driver.page_source

                if "Atividades Complementares" in page_content:
                    # Verificar se o usuário já existe
                    user, created = User.objects.get_or_create(username=matricula)
                    
                    if created:
                        # Define a senha e salva o usuário, caso seja uma nova conta
                        user.set_password(senha)
                        user.save()

                    # Autenticar e realizar o login
                    user = authenticate(request, username=matricula, password=senha)
                    login(request, user)
                    #! LOGIN FEITO COM SUCESSO
                    nome = driver.find_element(By.XPATH, "//li[@id='liUsuarioMatricula']//span[@id='lblNomeUsuario']/b").text

                    usuario, created = Usuario.objects.get_or_create(nome_usuario=nome, user=user, matricula=matricula,tipo_de_usuario='Aluno')

                    context = {'usuario' : usuario}

                    driver.quit()
                    return redirect('/pucAgora/feed')
                else:
                    #!LOGIN FALHOU
                    request.session['error'] = 'Login falhou. Verifique seus dados e tente novamente.'
                    driver.quit()
                    return redirect('fazer_login')

            #! PROBLEMA NO DRIVER
            except (NoSuchElementException, WebDriverException):
                request.session['error'] = 'Erro ao realizar o login. Tente novamente mais tarde.'
                return redirect('fazer_login')
        else :
            login(request, user)
            usuario = Usuario.objects.get(matricula=matricula, user=user)
            context = {'usuario' : user}
            return redirect('/pucAgora/feed')


    #! USUARIO REINICIA A PAGINA
    error = request.session.pop('error', None)
    return render(request, 'login.html', {'error': error})


@login_required
def perfil(request) :
    context = {}
    return render(request, "Perfil.html", context)

@login_required
def calendario(request) :
    context = {}
    return render(request, "Calendario.html", context)
@login_required
def meu_curso(request) :
    context = {}
    return render(request, "MeuCurso.html", context)

@login_required
def puc_agora(request) :
    context = {}
    return render(request, "PucAgora.html", context)


@login_required
def feed(request) :
    usuario = request.usuario
    context = {'usuario': usuario}
    return render(request, "PucAgora/Feed.html", context)

@login_required
def mapa(request) :
    context = {}
    return render(request, "PucAgora/Mapa.html", context)

@login_required
def siuni_mais(request) :
    context = {}
    return render(request, "PucAgora/SiuniMais.html", context)


@login_required
def homepage(request):
    # Obter todos os usuários e as informações associadas
    usuarios = Usuario.objects.select_related('aluno', 'professor').all()
    
    # Obter todas as turmas e avaliações
    turmas = Turma.objects.all()
    avaliacoes = Avaliacao.objects.all()

    # Obter todas as notas, faltas e médias finais
    notas = Nota.objects.all()
    faltas = Falta.objects.all()
    medias_finais = MediaFinal.objects.all()

    # Todos os professores
    professores = Professor.objects.all()

    context = {
        'professores': professores,
        'usuarios': usuarios,
        'turmas': turmas,
        'avaliacoes': avaliacoes,
        'notas': notas,
        'faltas': faltas,
        'medias_finais': medias_finais,
    }

    return render(request, 'homepage.html', context)




@login_required
def carregar_modal(request, modal_name):
    try:
        # Contexto para o modal (adicione as variáveis que desejar)
        context = {
            'titulo': 'SIUNI',
            'subtitulo': 'Quem Somos Nós?',
            'descricao': 'O SIUNI é um projeto idealizado e programado por Davi Donato e sua turma.'
        }

        # Renderiza o modal com base no nome passado
        return render(request, f'Modais/{modal_name}.html', context)
    except Exception as e:
        return HttpResponse(f"<h1>Erro ao carregar o modal: {e}</h1>", status=404)
    


@login_required
def fazer_logout(request) :
    logout(request)
    return redirect('fazer_login')


def custom_404_view(request, exception):
    if not request.user.is_authenticated:
        # Redireciona para a tela de login se o usuário não estiver autenticado
        return redirect('fazer_login')
    else:
        # Mostra uma página de erro personalizada se o usuário estiver logado
        return render(request, '404.html', status=404)
    



