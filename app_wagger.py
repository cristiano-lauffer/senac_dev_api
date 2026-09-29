from flask import Flask, request
from flasgger import Swagger, swag_from
from controllers.serie_controller import SerieController
from config.swagger import (
    get_all_spec,
    get_by_id_spec,
    buscar_termo_spec,
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
    "specs_route": "/series/swagger"
}

swagger = Swagger(app, config=swagger_config)


@app.route('/series', methods=['GET'])
@swag_from(get_all_spec)
def listar_todas():
    return SerieController.mostrar_tudo()

@app.route('/series/<int:serie_id>', methods=['GET'])
@swag_from(get_by_id_spec)
def listar_por_id(serie_id):
    return SerieController.mostrar_por_id(serie_id)

@app.route('/series/categoria/<string:termo>', methods=['GET'])
@swag_from(buscar_termo_spec)
def buscar_categoria(termo):
    return SerieController.mostrar_por_categoria(termo)

@app.route('/series/titulo/<string:termo>', methods=['GET'])
@swag_from(buscar_termo_spec)
def buscar_titulo(termo):
    return SerieController.mostrar_por_titulo(termo)

@app.route('/series/pais/<string:termo>', methods=['GET'])
@swag_from(buscar_termo_spec)
def buscar_pais(termo):
    return SerieController.mostrar_por_pais(termo)

@app.route('/series/idioma/<string:termo>', methods=['GET'])
@swag_from(buscar_termo_spec)
def buscar_idioma(termo):
    return SerieController.mostrar_por_idioma(termo)

@app.route('/series/idade/<string:termo>', methods=['GET'])
@swag_from(buscar_termo_spec)
def buscar_idade(termo):
    return SerieController.mostrar_por_idade(termo)

@app.route('/series', methods=['POST'])
@swag_from(insert_spec)
def criar():
    dados = request.json
    return SerieController.cadastrar(dados)

@app.route('/series/<int:serie_id>', methods=['PUT'])
@swag_from(update_spec)
def atualizar(serie_id):
    dados = request.json
    return SerieController.atualizar(serie_id, dados)

@app.route('/series/<int:serie_id>', methods=['DELETE'])
@swag_from(delete_spec)
def deletar(serie_id):
    return SerieController.excluir(serie_id)

if __name__ == '__main__':
    app.run(debug=True)