get_all_spec = {
    "responses": {
        "200": {
            "description": "Lista de carros retornada com sucesso",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "oid_carro": {"type": "integer"},
                        "nom_carro": {"type": "string"},
                        "nom_marca": {"type": "string"},
                        "num_ano_fabricacao": {"type": "integer"},
                        "num_ano_modelo": {"type": "integer"},
                        "nom_cor": {"type": "string"},
                        "nom_combustivel": {"type": "string"},
                        "num_placa": {"type": "string"}
                    }
                }
            }
        }
    }
}

get_by_id_spec = {
    "parameters": [
        {
            "name": "carro_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do Carro"
        }
    ],
    "responses": {
        "200": {"description": "Carro encontrado com sucesso"},
        "404": {"description": "Carro não encontrado"}
    }
}

insert_spec = {
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "nom_carro": {"type": "string"},
                    "nom_marca": {"type": "string"},
                    "num_ano_fabricacao": {"type": "integer"},
                    "num_ano_modelo": {"type": "integer"},
                    "nom_cor": {"type": "string"},
                    "nom_combustivel": {"type": "string"},
                    "num_placa": {"type": "string"}
                }
            }
        }
    ],
    "responses": {
        "201": {"description": "Carro cadastrado com sucesso"}
    }
}

update_spec = {
    "parameters": [
        {
            "name": "carro_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do carro"
        },
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "nom_carro": {"type": "string"},
                    "nom_marca": {"type": "string"},
                    "num_ano_fabricacao": {"type": "integer"},
                    "num_ano_modelo": {"type": "integer"},
                    "nom_cor": {"type": "string"},
                    "nom_combustivel": {"type": "string"},
                    "num_placa": {"type": "string"}
                }
            }
        }
    ],
    "responses": {
        "200": {"description": "Carro atualizado com sucesso"},
        "404": {"description": "Carro não encontrado"}
    }
}

delete_spec = {
    "parameters": [
        {
            "name": "carro_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID do Carro"
        }
    ],
    "responses": {
        "200": {"description": "Carro removido com sucesso"},
        "404": {"description": "Carro não encontrado"}
    }
}