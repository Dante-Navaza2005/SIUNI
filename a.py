from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Inicializando o Chrome

chrome_options = Options()
chrome_options.add_argument("--headless")

chrome_options.add_argument("--no-sandbox")

chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Abrindo um site

driver.get('https://sau.puc-rio.br/WebLoginPucOnline/Default.aspx?sessao=VmluY3Vsbz1BJlNpc3RMb2dpbj1QVUNPTkxJTkVfQUxVTk8mQXBwTG9naW49TE9HSU4mRnVuY0xvZ2luPUxPR0lOJlNpc3RNZW51PVBVQ09OTElORV9BTFVOTyZBcHBNZW51PU1FTlUmRnVuY01lbnU9TUVOVQ__')
sleep(1)

CaixaMatricula = driver.find_element(By.CSS_SELECTOR, 'input#txtLogin')
CaixaMatricula.send_keys("2320399")
sleep(1)

CaixaSenha = driver.find_element(By.CSS_SELECTOR, 'input#txtSenha')
CaixaSenha.send_keys("DGB.1110")
sleep(1)

CaixaBotao = driver.find_element(By.CSS_SELECTOR, '#btnOk')
CaixaBotao.click()
sleep(2)


print("Entrei")
URL = driver.page_source
print(f"{URL}")

sleep(120)

# Encontrando um elemento e interagindo

driver.quit()