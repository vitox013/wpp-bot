from numpy import append
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

repetir = 1
prim_vez = 1

while(repetir):
    opcao_msg = 0
    
    while(opcao_msg != 1 and opcao_msg != 2):
        print('Gostaria de enviar a partir de uma lista txt ou palavras/msg especificas?')
        print('1 - Lista txt')
        print('2 - Palavras/msg especificas\n')
        opcao_msg = int(input())
        if(opcao_msg == 1):
            nome_txt = input('\nDigite o nome do arquivo igual na pasta (incluir ".txt" no final) ou o caminho dele no seu pc: ')


    print(nome_txt)
    contatos = []
    qnt_contatos = int(input('\nQuantos contatos? \n'))

    for j in range(qnt_contatos):
        nome_contato = input('Nome: ')
        contatos.append(nome_contato)


    if(opcao_msg == 1):
    
        
        if(prim_vez):
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get('https://web.whatsapp.com/')
            print('30 Segundos para scanear o QRCODE\n')
            qrcode = 0
            while(qrcode != 1):
                qrcode = int(input('Já leu o QRCODE?\n 1 - SIM\n 0 - NAO\n'))


        def buscar_contato(contato):
            campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
            time.sleep(3)
            campo_pesquisa.click()
            campo_pesquisa.send_keys(contato)
            campo_pesquisa.send_keys(Keys.ENTER)

        def enviar_mensagem():
            campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
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

# driver = webdriver.Chrome(ChromeDriverManager().install())

# if(opcao_msg == 1):

# driver.get('https://web.whatsapp.com/') 

#          #nome dos contatos(tem que ser exatamente igual)

# def buscar_contato(contato): #funcao que busca o contato
#     campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
#     time.sleep(3)
#     campo_pesquisa.click()
#     campo_pesquisa.send_keys(contato)
#     campo_pesquisa.send_keys(Keys.ENTER)

# def enviar_mensagem():  #funcao que envia as msg
#     campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
#     campo_mensagem[1].click()
#     with open('lista.txt', 'r') as arquivo:  #inserir como parametro do open o endereco do arquivo txt (ou o nome caso esteja na mesma pasta)
#         for mensagem in arquivo:
#             campo_mensagem[1].send_keys(mensagem)
#             campo_mensagem[1].send_keys(Keys.ENTER)

# for contato in contatos:            #envia pra cada contato que estivar no vetor contatos
#     buscar_contato(contato)
#     enviar_mensagem()