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
from django.shortcuts import get_object_or_404
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains






from .utils import *

def fazer_login(request):
    error = None

    #! FAZENDO O LOGIN
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        senha = request.POST.get('senha')

        if matricula == '' or senha == '' :
            request.session['error'] = 'Preencha os campos corretamente'
            return redirect('fazer_login')

        user = authenticate(username=matricula, password=senha)

        if not user :
            # Configuração do Selenium para login automático

            try:
                # Inicia o ChromeDriver automaticamente usando webdriver-manager
                driver = webdriver.Chrome()

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

                    #!ENTRANDO EM SITUACAO ACADEMICA
                    element = driver.find_element(By.XPATH, "//a[@title='Situação Acadêmica']")

                    # Clicar no elemento
                    element.click()
                    sleep(1)

                    #?PEGANDO PERIODO
                    select_element = driver.find_element(By.ID, "ddlPeriodo")
                    dropdown = Select(select_element)
                    
                    sleep(1)

                    # Obter a quantidade de opções no dropdown
                    periodo = len(dropdown.options) - 1

                    #curso = driver.find_element(By.ID, "tbcCurso").text

                    usuario, created = Usuario.objects.get_or_create(nome_usuario=nome, user=user, matricula=matricula,tipo_de_usuario='Aluno')

                    aluno, created = Aluno.objects.get_or_create(usuario=usuario, numero_periodo=periodo)

                    driver.quit()
                    return redirect('/pucAgora/feed')
                else:
                    #!LOGIN FALHOU
                    request.session['error'] = 'Dados inválidos. Tente novamente.'
                    driver.quit()
                    return redirect('fazer_login')

            #! PROBLEMA NO DRIVER
            except (WebDriverException):
                request.session['error'] = 'Erro ao realizar o login. Teste mais tarde ou em outro browser.'
                return redirect('fazer_login')
        else :
            login(request, user)
            return redirect('/pucAgora/feed')


    #! USUARIO REINICIA A PAGINA
    error = request.session.pop('error', None)
    return render(request, 'login.html', {'error': error})




@login_required
def perfil(request) :
    aluno = request.aluno
    context = {'aluno': aluno}
    return render(request, "Perfil.html", context)

@login_required
def calendario(request) :
    aluno = request.aluno
    context = {'aluno': aluno}
    return render(request, "Calendario.html", context)
@login_required
def meu_curso(request) :
    aluno = request.aluno
    context = {'aluno': aluno}
    return render(request, "MeuCurso.html", context)

@login_required
def puc_agora(request) :
    aluno = request.aluno
    context = {'aluno': aluno}
    return render(request, "PucAgora.html", context)


@login_required
def feed(request) :
    aluno = request.aluno
    noticia = Noticia.objects.all()
    context = {'aluno': aluno, 'noticias': noticia}
    return render(request, "PucAgora/Feed.html", context)

@login_required
def mapa(request) :
    aluno = request.aluno
    context = {'aluno': aluno}
    return render(request, "PucAgora/Mapa.html", context)

@login_required
def siuni_mais(request) :
    usuario = request.usuario
    context = {'usuario': usuario}
    # Obtém os posts do usuário atual
    posts = Post.objects.filter(usuario=request.usuario)

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')

        # Verifica se os campos foram preenchidos
        if titulo and descricao:
            Post.objects.create(usuario=request.usuario, titulo=titulo, descricao=descricao)
            return redirect('siuni_mais')  # Redireciona após criar o post
    
    context.update({'posts': posts})
    return render(request, 'PucAgora/SiuniMais.html', context)


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
    usuario = request.usuario
    context = {'usuario': usuario}
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



@login_required
def apagar_post(request, post_id):
    usuario = request.usuario
    context = {'usuario': usuario}
    post = get_object_or_404(Post, id=post_id, usuario=request.usuario)
    if request.method == 'POST':
        post.delete()
        return redirect('siuni_mais')


@login_required
def editar_post(request, post_id):
    usuario = request.usuario
    context = {'usuario': usuario}
    post = get_object_or_404(Post, id=post_id, usuario=request.usuario)
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')

        if titulo and descricao:
            post.titulo = titulo
            post.descricao = descricao
            post.save()
            return redirect('siuni_mais')

    return render(request, 'PucAgora/editar_post.html', {'post': post})
