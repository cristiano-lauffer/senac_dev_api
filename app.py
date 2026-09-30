from flask import Flask, request
from flasgger import Swagger, swag_from
from controllers.carro_controller import CarroController
from config.swagger import (
    get_all_spec,
    get_by_id_spec,
    insert_spec,
    update_spec,
    delete_spec
)

app = Flask(__name__)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda rule: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/carros/swagger"
}

swagger = Swagger(app, config=swagger_config)

@app.route('/carros', methods=['GET'])
@swag_from(get_all_spec)
def listar_todas():
    return CarroController.mostrar_tudo()

@app.route('/carros/<int:carro_id>', methods=['GET'])
@swag_from(get_by_id_spec)
def listar_por_id(carro_id):
    return CarroController.mostrar_por_id(carro_id)

@app.route('/carros', methods=['POST'])
@swag_from(insert_spec)
def criar():
    dados = request.json
    return CarroController.cadastrar(dados)

@app.route('/carros/<int:carro_id>', methods=['PUT'])
@swag_from(update_spec)
def atualizar(carro_id):
    dados = request.json
    return CarroController.atualizar(carro_id, dados)

@app.route('/carros/<int:carro_id>', methods=['DELETE'])
@swag_from(delete_spec)
def deletar(carro_id):
    return CarroController.excluir(carro_id)

if __name__ == '__main__':
    app.run(debug=True)