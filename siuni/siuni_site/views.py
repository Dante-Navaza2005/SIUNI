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

def fazer_login(request):
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        senha = request.POST.get('senha')

        # Configuração do Selenium para login automático
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")

        try:
            # Inicia o ChromeDriver automaticamente usando webdriver-manager
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

            # Acessar o site do SAU e realizar o login
            driver.get('https://sau.puc-rio.br/WebLoginPucOnline/Default.aspx?sessao=VmluY3Vsbz1BJlNpc3RMb2dpbj1QVUNPTkxJTkVfQUxVTk8mQXBwTG9naW49TE9HSU4mRnVuY0xvZ2luPUxPR0lOJlNpc3RNZW51PVBVQ09OTElORV9BTFVOTyZBcHBNZW51PU1FTlUmRnVuY01lbnU9TUVOVQ__')
            sleep(1)

            # Preencher os campos de login e senha
            CaixaMatricula = driver.find_element(By.CSS_SELECTOR, 'input#txtLogin')
            CaixaMatricula.send_keys(matricula)
            sleep(1)

            CaixaSenha = driver.find_element(By.CSS_SELECTOR, 'input#txtSenha')
            CaixaSenha.send_keys(senha)
            sleep(1)

            # Clicar no botão de login
            CaixaBotao = driver.find_element(By.CSS_SELECTOR, '#btnOk')
            CaixaBotao.click()
            sleep(2)

            # Verificar se o login foi bem-sucedido
            page_content = driver.page_source
            driver.quit()
            
            if "Atividades Complementares" in page_content:
                return redirect('homepage')  # Redireciona para evitar reenvio de formulário
            else:
                # Armazena a mensagem de erro na sessão para exibir após o redirecionamento
                request.session['error'] = 'Login falhou. Verifique seus dados e tente novamente.'
                return redirect('fazer_login')

        except (NoSuchElementException, WebDriverException):
            request.session['error'] = 'Erro ao realizar o login. Tente novamente mais tarde.'
            return redirect('fazer_login')

    # Carrega a mensagem de erro da sessão, se existir
    error = request.session.pop('error', None)
    return render(request, 'Login.html', {'error': error})

def perfil(request) :
    context = {}
    return render(request, "Perfil.html", context)

def calendario(request) :
    context = {}
    return render(request, "Calendario.html", context)

def meu_curso(request) :
    context = {}
    return render(request, "MeuCurso.html", context)

def puc_agora(request) :
    context = {}
    return render(request, "PucAgora.html", context)


def feed(request) :
    context = {}
    return render(request, "PucAgora/Feed.html", context)

def mapa(request) :
    context = {}
    return render(request, "PucAgora/Mapa.html", context)

def siuni_mais(request) :
    context = {}
    return render(request, "PucAgora/SiuniMais.html", context)


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