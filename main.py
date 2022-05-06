from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://web.whatsapp.com/')
time.sleep(30)                  #tempo de espera para ler o qrcode

contatos = ['teste.py', 'My']         #nome dos contatos(tem que ser exatamente igual)
mensagem = []


def buscar_contato(contato): #funcao que busca o contato
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):  #funcao que envia as msg
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    with open('lista.txt', 'r') as arquivo:  #inserir como parametro do open o endereco do arquivo txt (ou o nome caso esteja na mesma pasta)
        for mensagem in arquivo:
            campo_mensagem[1].send_keys(mensagem)
            campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:            #envia pra cada contato que estivar no vetor contatos
    buscar_contato(contato)
    enviar_mensagem(mensagem)