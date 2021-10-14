#Pré-Requisitos para rodar a Aplicação

É necessário instalar as bibliotecas abaixo

Abra esse projeto na IDE Python e execute os seguintes comandos:
```
pip install flask
pip install flask_pydantic_spec 
```

## Rodando a aplicação

Para rodar a aplicação você precisa execeutar o seguinte comando: 

```
flask run
```

O sistema vai devolver o endereço do server(Geralmente: http://127.0.0.1:5000/).
Acesse a documentação da API(Swagger) pelo seu navegador(Google Chrome) na URL abaixo:

```
http://127.0.0.1:5000/apidoc/swagger
```
É possível executar os recursos direto da documentação /swagger. 
Se preferir utilize um client http de sua preferência.

## Visualização dos recebimentos

Execute as chamadas nos seguintes recursos:

Para saber sobre o Maurício, execute:
/perfil - GET

Para saber sobre porque quero participar deste programa de estágio, execute:
/programa - GET

Para saber quais os motivos me motivam para ingressar na área de t.i, execute:
/motivadores - GET

Para saber os motivos que me levaram escolher a Ingram, execute:
/ingram - GET

Para conhecer o objeto de grande significado para mim, execute:
/objeto - GET



#Objetivos da aplicação:
Apresentar um objeto pessoal que tenha significado na sua vida,
e que você consiga utilizá-lo para se descrever no final da apresentação.

Regras:

Use e abuse da sua criatividade para fazer uma apresentação diferenciada.

Tempo para apresentação: 20 minutos.

O candidato deverá fazer a apresentação utilizando as linguagens de programação que tiver conhecimento.

Apresentar os seguintes aspectos:

Quem sou eu?
Família, Lazer, Finanças, Acadêmico,  Profissional, Busca de Aprendizado e Futuro.
Qual a importância deste programa de Estágio na sua vida?
Por que você deve ser o novo Estagiário da área de TI?
Por que a Ingram e não outra empresa?

