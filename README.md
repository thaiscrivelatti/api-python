# api-python

Desenvolver uma api escrita em python/flask que implemente funções de apoio para um suposto frontend.
Todas as funções, quando necessário, devem ler e/ou devolver dados em formato json
As funções a serem implementadas são:
- Conversão de temperatura entre as unidades Kelvin, Celcius e Fahrenheit
- Consultar CEP de uma API externa (postmon, viacep, widenet, etc...)

Ferramentas utilizadas:
- Python 3.0
- Visual Studio Code

Para executar o projeto:
- No terminal executar os comandos:
  - pip install flask para instalar os pacotes do flask
  - pip install requests para instalar os pacotes de requests
  - python main.py para executar a aplicação
- A aplicação rodará no localhost, porta 5000 (http://127.0.0.1:5000/)
- As requisições utilizadas para se comunicar com a API estão commitadas junto com o projeto, arquivo "api-python.postman_collection".

Material consultado:
- http://devfuria.com.br/python
- https://www.dataquest.io/blog/python-api-tutorial/
- https://rapidapi.com/blog/how-to-build-an-api-in-python/