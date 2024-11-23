from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def preencher_login(driver, matricula, senha) :
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