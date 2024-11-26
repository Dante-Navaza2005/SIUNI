from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless=new")

driver = webdriver.Chrome(service=service, options=options)

# Abre o site em segundo plano
driver.get('http://selenium.dev/')

# Obtém e imprime o conteúdo da página
conteudo = driver.page_source
print(conteudo)

# Fecha o navegador
driver.quit()
