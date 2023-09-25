
# store frontend
Este pequeno projeto é parte do material didático da disciplina Desenvolvimento Full Stack Avamçado da PUC-Rio. A ideia inicial do projeto como escopo era realizar o cadastro de pedidos, produtos e usuários, esse projeto consiste em um loja on line onde serão vendidos diversos produtos.
Esse Projeto back-end foi construído em python com o framework flask, html, boostrap e javascript.

O front end da aplicação vai se comunicar com a api do usuário através do micro serviço de usuário para registrar o usuário e se logar no sistema, bem como realizará a comunicação com o microserviço de produto para resgatar os produtos cadastrados no sistema, assim como vinculará os ítens ao carrinho e no final efetuará o checkout desse carrinho. Abaixo está definido o diagrama arquitetural.

Diagrama arquitetural (Micro Serviços)
<br />![image](https://github.com/franklinpr2010/frontend/assets/2296319/dad1d9dd-2ba1-4d5a-991b-ed737bbe2c3a)


<br />Rode os seguintes comandos na maquina local:
<br />1 - Criar o ambiente virtual no venv para executar o projeto. Execute os seguintes comandos no console.
<br /> pip install virtualenv

2 - Criar o ambiente virtual
<br /> python -m venv virtualmachine

3 - Depois de instalado o ambiente virtual executar o activate para executar o ambiente virtual.
<br /> cd .\virtualmachine\Scripts\ 

4 - Rode o comando para instalar as dependências
<br /> pip -r requirements.txt

5 - Execute o projeto:
<br /> py [diretódio do projeto]/app.py

Acesse: http://192.168.2.103:5000
























