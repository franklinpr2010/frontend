
# Store frontend
Este pequeno projeto é parte do material didático da disciplina Desenvolvimento Full Stack Avançado da PUC-Rio. A ideia inicial do projeto como escopo era realizar o cadastro de pedidos, produtos e usuários, esse projeto consiste em um loja on line onde serão vendidos diversos produtos.
Esse Projeto back-end foi construído em python com o framework flask, html, boostrap e javascript.

O front end da aplicação vai se comunicar com a api do usuário através do micro serviço de usuário para registrar o usuário e se logar no sistema, bem como realizará a comunicação com o microserviço de produto para resgatar os produtos cadastrados no sistema, assim como vinculará os ítens ao carrinho e no final efetuará o checkout desse carrinho. Abaixo está definido o diagrama arquitetural.

Diagrama arquitetural (Micro Serviços)
<br />![image](https://github.com/franklinpr2010/frontend/assets/2296319/a3cc66e8-01dc-49b4-b48c-b02cbb93b7c7)

https://drive.google.com/file/d/1sil-2nBTrgQKDYofLNY93P1lrryAhxxw/view?usp=sharing

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


Manual do usuário.

# Adicionar produto e concluir compra.

1) Acesse a página inicial http://192.168.2.103:5000,essa página mostrara os produtos cadastrados

![image](https://github.com/franklinpr2010/frontend/assets/2296319/a9f32a8c-69f8-4cae-8e22-d26beb8080ac)

2) Para adicionar o produto ao carrinho basta clicar no botão ver detalhes.

![image](https://github.com/franklinpr2010/frontend/assets/2296319/a004bb0d-7c4e-41fb-9fac-fe1822d85af3)

3) Ao clica em ver detalhes o sistema mostrará o produto e o botão com a opção 'Adicionar ao carrinho'.

![image](https://github.com/franklinpr2010/frontend/assets/2296319/7cfd0fbb-c928-41ae-87bd-6d715cb4eefd)

4) Ao clicar em adicionar carrinho ele vai enviar a tela de login, use o usuário e senha, senão tiver usuário cadastre um usuário no menu 'Cadastro de usuário'

![image](https://github.com/franklinpr2010/frontend/assets/2296319/e0d9605a-f833-44bc-af52-abc5ebb88ca3)

5) Ao logar você será redirecionado para a tela de detalhes onde poderá adicionar ao carrinho.

![image](https://github.com/franklinpr2010/frontend/assets/2296319/24585690-3080-4f6f-9956-cff91bf2e02b)

6) Ao clicar em Adicionar ao carrinho aparecerá um balão no menu em checkout informando que adicionou um item ao carrinho.

![image](https://github.com/franklinpr2010/frontend/assets/2296319/bfa8b9a2-a4c7-46b8-9f6d-4930e4f35b1c)

7) Ao clicar em checkout finalizará a compra e será concluída.

![image](https://github.com/franklinpr2010/frontend/assets/2296319/459ac0d8-1c80-4abb-bafd-bacc186bb652)

# Cadastro de usuário

1) Clique no menu cadastrar usuário.

![image](https://github.com/franklinpr2010/frontend/assets/2296319/98f726a2-8f9c-49d5-9138-30e02cff09e7)

2) Cadastre os campos usuário, senha e informe um cep válido e clique em enviar.

Apresentação

https://drive.google.com/file/d/1mL98PzxrlewdF0YJeA76H35CW1shQGii/view



   
























