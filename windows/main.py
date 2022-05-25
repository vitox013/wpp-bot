from numpy import append
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os 


class wpp_bot:
    repetir = 1
    prim_vez = 1
    def iniciar(self):
        while(self.repetir):
            self.nome_do_txt_e_contatos()
            self.ler_qr_code_e_logar()
            self.execucao()
            self.ask_repetir()

    def nome_do_txt_e_contatos(self):
        self.nome_txt = input('\nDigite o nome do arquivo igual na pasta (incluir ".txt" no final) ou o caminho dele no seu pc: ')

        print(self.nome_txt)
        qnt_contatos = int(input('\nQuantos contatos? \n'))
        self.contatos = []

        for j in range(qnt_contatos):
            nome_contato = input('Nome: ')
            self.contatos.append(nome_contato)

    def ler_qr_code_e_logar(self):
        if(self.prim_vez):
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.driver.get('https://web.whatsapp.com/')
            print('Leia o QRCODE para entrar no WhatsApp\n')
            qrcode = 0
            while(qrcode != 1):
                qrcode = int(input('\nJá leu o QRCODE?\n 1 - SIM\n 0 - NAO\n'))

    def buscar_contato(self, contato, ):
        campo_pesquisa = self.driver.find_element(By.XPATH,'//div[contains(@class,"copyable-text selectable-text")]')
        time.sleep(3)
        campo_pesquisa.click()
        campo_pesquisa.send_keys(contato)
        campo_pesquisa.send_keys(Keys.ENTER)

    def colar_e_enviar_mensagem(self):
        campo_mensagem = self.driver.find_elements(By.XPATH,'//div[contains(@class,"copyable-text selectable-text")]')
        campo_mensagem[1].click()
        CURR_DIR = os.getcwd()
        with open(CURR_DIR + "/listasTXT/" + self.nome_txt, 'r') as arquivo:
            for mensagem in arquivo:
                campo_mensagem[1].send_keys(mensagem)
                campo_mensagem[1].send_keys(Keys.ENTER)

    def execucao(self):
        for contato in self.contatos:           
            self.buscar_contato(contato)
            self.colar_e_enviar_mensagem()

    def ask_repetir(self):
        self.repetir = int(input('Deseja rodar novamente?\n 1 - SIM\n 0 - NÃO\n'))
        self.prim_vez = 0


start = wpp_bot()
start.iniciar()
