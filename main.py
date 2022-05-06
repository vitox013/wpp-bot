from numpy import append
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


repetir = 1
prim_vez = 1

while(repetir):
       
    nome_txt = input('\nDigite o nome do arquivo igual na pasta (incluir ".txt" no final) ou o caminho dele no seu pc: ')


    print(nome_txt)
    contatos = []
    qnt_contatos = int(input('\nQuantos contatos? \n'))

    for j in range(qnt_contatos):
        nome_contato = input('Nome: ')
        contatos.append(nome_contato)

    
    if(prim_vez):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://web.whatsapp.com/')
        print('Leia o QRCODE para entrar no WhatsApp\n')
        qrcode = 0
        while(qrcode != 1):
            qrcode = int(input('\nJá leu o QRCODE?\n 1 - SIM\n 0 - NAO\n'))


    def buscar_contato(contato):
        campo_pesquisa = driver.find_element(By.XPATH,'//div[contains(@class,"copyable-text selectable-text")]')
        time.sleep(3)
        campo_pesquisa.click()
        campo_pesquisa.send_keys(contato)
        campo_pesquisa.send_keys(Keys.ENTER)

    def enviar_mensagem():
        campo_mensagem = driver.find_elements(By.XPATH,'//div[contains(@class,"copyable-text selectable-text")]')
        campo_mensagem[1].click()
        with open(nome_txt, 'r') as arquivo:
            for mensagem in arquivo:
                campo_mensagem[1].send_keys(mensagem)
                campo_mensagem[1].send_keys(Keys.ENTER)

    for contato in contatos:           
        buscar_contato(contato)
        enviar_mensagem()

    repetir = int(input('Deseja rodar novamente?\n 1 - SIM\n 0 - NÃO\n'))
    prim_vez = 0