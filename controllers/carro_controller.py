from flask import jsonify
from models.carro import CarroModel

class CarroController:
    @staticmethod
    def mostrar_tudo():
        carros = CarroModel.get_all()
        return jsonify(carros)

    @staticmethod
    def mostrar_por_id(carro_id):
        carro = CarroModel.get_by_id(carro_id)
        if carro:
            return jsonify(carro)
        return jsonify({"erro": "Carro não encontrado"}), 404

    @staticmethod
    def cadastrar(dados):
        novo_id = CarroModel.insert(dados)
        return jsonify({"mensagem": "Carro criada com sucesso", "id": novo_id}), 201

    @staticmethod
    def atualizar(carro_id, dados):
        sucesso = CarroModel.update(carro_id, dados)
        if sucesso:
            return jsonify({"mensagem": "Carro atualizada com sucesso"})
        return jsonify({"erro": "Carro não encontrado", "código": "404"}), 404

    @staticmethod
    def excluir(carro_id):
        sucesso = CarroModel.delete(carro_id)
        if sucesso:
            return jsonify({"mensagem": "Carro excluída com sucesso"})
        return jsonify({"erro": "Carro não encontrado", "código": "404"}), 404