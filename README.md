# WhatsApp Bot :robot:
 Um bot simples de envio de mensagens em massa a partir de um arquivo txt para N contatos
 
 ## Instalações necessárias
 
<div>
 
 ### Linux
 * Vá até uma pasta de sua preferência e digite: 
 ```shell
 git clone https://github.com/vitox013/wpp-bot.git
 ```
 * Será necessario ter o [python3](https://www.python.org/downloads/) instalado (já vem pré-instalado no Ubuntu 20.04 e outras versões do debian linux)
 * Instalar o [selenium](https://www.selenium.dev/), abra seu terminal e digite:
 ```shell
 sudo pip3 install selenium==4.1.4
 ```
 * Instalar o [webdriver_manager](https://pypi.org/project/webdriver-manager/), abra seu terminal e digite:
 ```shell
 sudo pip3 install webdriver_manager
 ```
 
 </div>
 <hr>
 <div>
 
 ### Windows
 
  * Vá até uma pasta de sua preferência e digite no terminal: 
 ```shell
 git clone https://github.com/vitox013/wpp-bot.git
 ```
 * Será necessario ter o [python3](https://www.python.org/downloads/) instalado **e na instalação ter marcado a opção "add python to PATH"**
 #### Instalação Automática :robot:
 * Entrar na pasta "windows" e executar o arquivo **install-requirements.bat**, no qual irá instalar o que é necessário automaticamente.
 
 #### Instalação Manual 🧑‍🏭
 Caso queira instalar por conta própria basta:
 
 * Abrir o terminal e instalar o [selenium](https://www.selenium.dev/) digitando:
 
 ```shell
 pip install selenium==4.1.4
 ```
 * No mesmo terminal instalar o [webdriver_manager](https://pypi.org/project/webdriver-manager/) digitando:
 ```shell
 pip install webdriver_manager
 ```
 * Instalar uma biblioteca do python chamada **numpy** digitando:
 ```shell
 pip install numpy
 ```
 
 
 
 </div>
 
 ## Executar o bot
 * ### Colocar o arquivo txt escolhido dentro da pasta "listasTXT"
 
 * ### Linux
 Após todas as instalações, abra o terminal na pasta do bot e digite: 
 
 ```shell
 ./run.sh
 ```
 
 * ### Windows
 Após todas as instalações, executar o arquivo **run.bat** ou digitar no terminal:
 ```shell
 python main.py
 ```

 ## Preview
 
![gifwpp-bot](https://user-images.githubusercontent.com/85710199/167051785-a63ec25d-b712-4aff-9f3f-d8a6d62d94e2.gif)



Caso queira visualizar na velocidade real é só clicar no ícone abaixo:<br> 
[![Youtube Badge](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=A3RPoNRcsJ4)


