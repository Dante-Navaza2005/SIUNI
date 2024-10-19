import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep

def chrome_instalado():
    # Tenta localizar o binário do Chrome no sistema
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    return os.path.exists(chrome_path)

def iniciar_navegador():
    if chrome_instalado():
        print("Chrome encontrado, inicializando o Chrome...")
        chrome_options = Options()
        chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    else:
        print("Chrome não encontrado, inicializando o Safari...")
        driver = webdriver.Safari()  # Safari WebDriver não requer instalação adicional
    return driver

# Inicializa o navegador baseado na detecção
driver = iniciar_navegador()

# Abrindo um site
driver.get('https://sau.puc-rio.br/WebLoginPucOnline/Default.aspx?sessao=VmluY3Vsbz1BJlNpc3RMb2dpbj1QVUNPTkxJTkVfQUxVTk8mQXBwTG9naW49TE9HSU4mRnVuY0xvZ2luPUxPR0lOJlNpc3RNZW51PVBVQ09OTklORV9BTFVOTyZBcHBNZW51PU1FTlUmRnVuY01lbnU9TUVOVQ__')
sleep(1)

# Interagindo com a página
CaixaMatricula = driver.find_element(By.CSS_SELECTOR, 'input#txtLogin')
CaixaMatricula.send_keys("12345")
sleep(1)

CaixaSenha = driver.find_element(By.CSS_SELECTOR, 'input#txtSenha')
CaixaSenha.send_keys("12345")
sleep(1)

CaixaBotao = driver.find_element(By.CSS_SELECTOR, '#btnOk')
CaixaBotao.click()

sleep(120)

# Fechando o navegador
driver.quit()
