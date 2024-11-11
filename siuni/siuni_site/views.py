from django.shortcuts import render, redirect
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
from .models import *

# Create your views here.

def chrome_instalado():
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    return os.path.exists(chrome_path)

def iniciar_navegador():
    if chrome_instalado():
        chrome_options = Options()
        chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    else:
        driver = webdriver.Safari()
    return driver

def fazer_login(request):
    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        senha = request.POST.get('senha')

        driver = iniciar_navegador()
        driver.get('https://sau.puc-rio.br/WebLoginPucOnline/Default.aspx?sessao=VmluY3Vsbz1BJlNpc3RMb2dpbj1QVUNPTkxJTkVfQUxVTk8mQXBwTG9naW49TE9HSU4mRnVuY0xvZ2luPUxPR0lOJlNpc3RNZW51PVBVQ09OTklORV9BTFVOTyZBcHBNZW51PU1FTlUmRnVuY01lbnU9TUVOVQ__')
        
        sleep(1)
        CaixaMatricula = driver.find_element(By.CSS_SELECTOR, 'input#txtLogin')
        CaixaMatricula.send_keys(matricula)
        
        sleep(1)
        CaixaSenha = driver.find_element(By.CSS_SELECTOR, 'input#txtSenha')
        CaixaSenha.send_keys(senha)
        
        sleep(1)
        CaixaBotao = driver.find_element(By.CSS_SELECTOR, '#btnOk')
        CaixaBotao.click()
        
        sleep(10)  # Ajuste este tempo conforme necessário

        # Fechando o navegador
        driver.quit()
        
        return redirect('homepage')  # Redirecionar para uma página de sucesso após o login

    context = {}
    return render(request, 'login.html', context)

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

