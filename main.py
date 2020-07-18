# 18/07/2020 - Thais Crivelatti
# Desenvolver uma api escrita em python/flask que implemente funções de apoio para um suposto frontend.

from flask import Flask, jsonify, request
import json
app = Flask(__name__)

# Conversão de temperatura entre as unidades Kelvin, Celcius e Fahrenheit
@app.route("/converte", methods=['POST'])
def converte():
    requestData = request.json
    unidadeOrigem = requestData['UnidadeOrigem']
    unidadeDestino = requestData['UnidadeDestino']
    valor = requestData['Valor']
    valorConvertido = 0
    
    if (unidadeOrigem == 'C'):
        valorConvertido = valor + 273 if unidadeDestino == 'K' else (valor * 9/5) + 32
    elif (unidadeOrigem == 'F'): 
        valorConvertido = (valor - 32) * 5/9 if unidadeDestino == 'C' else (valor - 32) * 5/9 + 273
    else:
        valorConvertido = valor - 273 if unidadeDestino == 'C' else (valor - 273) * 9/5 + 32
    
    return jsonify({"ValorConvertido": valorConvertido})

if __name__ == "__main__":
    app.run()