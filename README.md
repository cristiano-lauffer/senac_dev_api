# senac_dev_api
Projeto da cadeira Desenvolvimento de Serviços e APIs (ADS3N26-2)

# Instalação e execução em desenvolvimento

## Database (MySQL)
Executar scrpts, em ordem, da pasta [_database](./_database).

## Criação do ambiente virtual (Windows)
Para execução em desenvolvimento, criar ambimente "venv enviroment" no Windows, conforme abaixo:

Abrir Powershel na pasta do projeto e rodar os comandos abaixo:

```powershell
python -m venv venv
 
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
 
.\venv\Scripts\Activate.ps1
 
pip install Flask mysql-connector-python flasgger

```

## Executar a aplicação
Ainda na mesma janela aberta, para rodar a aplicação:

```powershell
python app.py
```

## Consultando a api
Para rodar utilizando Swagger no navegador:

```http
http://localhost:5000/carros/swagger
```

Para rodar sem Swagger no navegador:

```http
http://localhost:5000/carros/
```
