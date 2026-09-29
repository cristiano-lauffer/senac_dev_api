from flask import Flask, request
# from flasgger import Swagger, swag_from
from controllers.carro_controller import CarroController

app = Flask(__name__)

@app.route('/carros', methods=['GET'])
def listar_todas():
    return CarroController.mostrar_tudo()

@app.route('/carros/<int:carro_id>', methods=['GET'])
def listar_por_id(carro_id):
    return CarroController.mostrar_por_id(carro_id)

@app.route('/carros', methods=['POST'])
def criar():
    dados = request.json
    return CarroController.cadastrar(dados)

@app.route('/carros/<int:carro_id>', methods=['PUT'])
def atualizar(carro_id):
    dados = request.json
    return CarroController.atualizar(carro_id, dados)

@app.route('/carros/<int:carro_id>', methods=['DELETE'])
def deletar(carro_id):
    return CarroController.excluir(carro_id)

if __name__ == '__main__':
    app.run(debug=True)