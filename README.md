<h1> Toro Backend </h1>

<p> Backend de uma aplicação destinada a permitir que usuarios comprem acoes, a verifiquem a tandencia do mercado. </p>

<p> Foi desenvolvida utilizando a linguagem python, junto com o framework fastapi, a orm sqlalchemy, e o banco de dados mysql</p>

<h2> Como executar o projeto Localmente</h2>
<h3> Dependecias</h3>
<ul>
  <li>ter o docker, e docker-compose instalado</li>
  <li>ter o python instalado</li>
  <li>ter o node e npm instalado</li>
  <li>um servidor mysql rodando no edpoint localhost:3306</li>
  <li>um banco de dados mysql chamado toro</li>
  <li>um banco de dados mysql chamado toro-test</li>
</ul>

<h3> Como Executar </h3>
<p> Execute os comandos na seguinte ordem:</p>
<p> utilize o arquivo docker-compose.yml localizado na raiz do projeto com o seguinte comando:</p>

```
docker-compose up
```

<p> aguarde a finalização do build dos containers</p>
<p> após os containers serem montados, execute o seguinte comando na raiz do projeto para criação das tabelas:</p>

```
npm run build:all
```
Estes dois comandos irão criar um container mysql no seguinte endereço:

```
localhost:3306
```

deve possuir os seguintes bancos de dados:

<ul>
  <li>toro</li>
  <li>toro-test</li>
</ul>

<h3> Conectar ao Banco de dados </h3>
<p> Voce pode usar as seguintes credenciais para tentar se conectar ao servidor sql:</p>
<ul>
  <li>user: root</li>
  <li>password: toro</li>
  <li>host: localhost</li>
  <li>porta: 3306</li>
  <li>nome do banco: toro</li>
</ul>

<h3> Conectar ao serviço </h3>
<p> Se tudo ocorreu bem, o backend estara sendo executado na porta 8080</p>
<p> Tente acessar a seguinte url para verificar a documentação do serviço</p>

```
http://localhost:8080/toro/doc/redoc  
```

<h2>Autenticação</h2>
Alguns serviços exigem altentição.<br>
Para utilizalos é necessario criar um usuario, obter um token de acesso no endpoint de autenticação com as credenciais deste usuario, e envia-lo da seguinte forma com campo authorization das headers "Bearer {access_token}"

<h2>Dados para Testes</h2>
Dentro da pasta db exite alguns arquivos sql que podem ser executados para adicionar dados no banco de dados para efeito de testes, caso decida utilizalos, eles devem ser executados na seguinte ordem:
<ol>
  <li>Assets</li>
  <li>Users</li>
  <li>Accounts</li>
  <li>user_assets</li>
  <li>orders</li>
</ol>

<h2>Executando o projeto sem ser pelo docker</h2>
<p> Para executar o projeto é necessario ter ter um banco de dados mysql rodando no endpoint localhost:3306, ele precisara de dois bancos de dados, um chamado toro, e outro chamado toro-test</p>

<p>primeiro instale as dependencias utilizando o comando:</p>

```
pip install -r requirements.txt
```
<br>
<p>utilize o seguinte comando para criar as tabelas tanto no banco toro quanto no banco toro-test:</p>

```
npm run build:all
```
<br>
<p>depois execute um dos comandos a seguir:</p>

```
npm start
```
<br>
<p>ou</p>

```
uvicorn app:app --host 0.0.0.0 --port 8080
```

<h2>Executando testes automatizados</h2>
<p> Para executar o projeto é necessario ter ter um banco de dados mysql rodando no endpoint localhost:3306, ele precisa ter o banco de dados toro-test</p>

<p>primeiro instale as dependencias utilizando o comando:</p>

```
pip install -r requirements.txt
```
<br>

<p>depois execute os testes utilizando o comando:</p>

```
npm run tests
```














