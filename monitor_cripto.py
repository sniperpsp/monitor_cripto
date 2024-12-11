from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

# Configuração do Selenium
driver_path = r"chromedriver.exe"  # Caminho do ChromeDriver
service = Service(driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Configuração da API do MercadoBitcoin
API_URL = "https://www.mercadobitcoin.net/api"
MOEDA = "WLD"
LIMITE_INFERIOR = 22.00
LIMITE_SUPERIOR = 23.00

# Dados da sua compra
PRECO_COMPRA = 22.87  # Preço que você pagou por unidade
QUANTIDADE_COMPRADA = 210.30  # Quantidade de moedas compradas

def iniciar_whatsapp():
    driver.get("https://web.whatsapp.com")
    print("Por favor, escaneie o QR Code para logar no WhatsApp Web.")
    time.sleep(15)

def enviar_mensagem(grupo, mensagem):
    try:
        search_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
        search_box.clear()
        search_box.send_keys(grupo)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)

        message_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )
        message_box.send_keys(mensagem)
        message_box.send_keys(Keys.ENTER)
        print(f"Mensagem enviada para o grupo '{grupo}'.")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

def monitorar_cripto(grupo):
    try:
        response = requests.get(f"{API_URL}/{MOEDA}/ticker/")
        data = response.json()["ticker"]

        price = float(data["last"])
        high = float(data["high"])
        low = float(data["low"])

        # Cálculo do lucro/prejuízo
        lucro_por_moeda = price - PRECO_COMPRA
        lucro_total = lucro_por_moeda * QUANTIDADE_COMPRADA
        status = "Lucro" if lucro_total > 0 else "Prejuízo"

        print(f"Preço atual: R${price:.2f}, {status} total: R${lucro_total:.2f}")

        mensagem = (
            f"Atualização do {MOEDA}\n"
            f"Preço atual: _R${price:.2f}_\n"
            f"Alta do dia: R${high:.2f}\n"
            f"Baixa do dia: R${low:.2f}\n"
            f"{status}: *R${lucro_total:.2f}* com base na compra de {QUANTIDADE_COMPRADA} moedas a R${PRECO_COMPRA:.2f}."
        )
        enviar_mensagem(grupo, mensagem)

    except Exception as e:
        print(f"Erro ao monitorar a criptomoeda: {e}")

if __name__ == "__main__":
    grupo = "Avisos Cripto" #colcoar seu grupo aqui
    iniciar_whatsapp()

    while True:
        monitorar_cripto(grupo)
        time.sleep(300)
