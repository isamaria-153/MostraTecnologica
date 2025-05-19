# REACT MANAGER: projeto analisador de sentimento
O objetivo do projeto é desenvolver um sistema capacitado para captar dados, analisar e gerenciar opiniões positivas ou negativas provenientes de comentários de usuários em redes sociais. O projeto buscará implementar técnicas de mineração de dados para classificar esses sentimentos e Processamento de Linguagem Natural, transportando comentários de uma determinada publicação para a sua análise sendo: "Positivo", "Negativo", "Neutro", podendo não identificar uma irônia (linguagem da atual geração).

## Diretório de Modelos

Este diretório armazena os modelos baixados pela biblioteca Transformers.
Seu ambiente de criação será o "venv"

## Como Executar a Aplicação
### Pré-requisitos
bibliotecas necessárias estão no "requirements.txt" e são:
- `fastapi==0.104.1`
- `uvicorn==0.23.2`
- `jinja2==3.1.2`
- `transformers==4.35.0`
- `torch==2.1.0`
- `sentencepiece==0.1.99`
- `protobuf==4.24.4`

terminal necessário: Command Prompt


### Passo a Passo
Instalando o venv: 
 `python -m venv venv`


 • Ativando o venv:
Entrar no terminal no vscode (Command prompt, no power shell da erro) na pasta geral digite o comando:
`venv\Scripts\activate`

 • Depois instale todos os requerimentos:
`pip install -r requirements.txt`

(Caso de erro, instale individualmente "pip install fastapi" ai vai ter que instalar todos, uvicorn, transformers...)

• Rode a api (certifique que o caminho esteja na pasta principal do projeto a APP pegando todos as outras pastas: app e venv( APP: app, venv)

`uvicorn app:app --reload`


• No terminal irá aparecer o endpoint, copie ele e cole no terminal adicionando /sent

(http://127.0.0.1:8000/)

• Teste com algum comentário na api online, mas deixe o terminal do vs code aberto para compilar.

