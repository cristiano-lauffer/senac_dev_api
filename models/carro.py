from config.conexao import get_connection
class CarroModel:
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
        SELECT
            oid_carro, nom_carro, nom_marca, num_ano_fabricacao, num_ano_modelo, nom_cor, nom_combustivel, num_placa
        FROM carros
        """)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_by_id(carro_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
        SELECT
            oid_carro, nom_carro, nom_marca, num_ano_fabricacao, num_ano_modelo, nom_cor, nom_combustivel, num_placa, dat_criacao, dat_alteracao
        FROM carros
        WHERE
            oid_carro = %s""", (carro_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def insert(dados):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO carros (nom_carro, nom_marca, num_ano_fabricacao, num_ano_modelo, nom_cor, nom_combustivel, num_placa) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (
            dados.get('nom_carro'),
            dados.get('nom_marca'),
            dados.get('num_ano_fabricacao'),
            dados.get('num_ano_modelo'),
            dados.get('nom_cor'),
            dados.get('nom_combustivel'),
            dados.get('num_placa')
        )
        cursor.execute(sql, valores)
        conn.commit()
        last_id = cursor.lastrowid
        cursor.close()
        conn.close()
        # raise Exception('(precisa ser implementado)')
        return last_id

    @staticmethod
    def update(carro_id, dados):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
        UPDATE carros SET
            nom_carro=%s,
            nom_marca=%s,
            num_ano_fabricacao=%s,
            num_ano_modelo=%s,
            nom_cor=%s,
            nom_combustivel=%s,
            num_placa=%s,
            dat_alteracao=CURRENT_TIMESTAMP()
        WHERE
            oid_carro=%s
        """
        valores = (
            dados.get('nom_carro'),
            dados.get('nom_marca'),
            dados.get('num_ano_fabricacao'),
            dados.get('num_ano_modelo'),
            dados.get('nom_cor'),
            dados.get('nom_combustivel'),
            dados.get('num_placa'),
            carro_id)
        cursor.execute(sql, valores)
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        conn.close()
        # raise Exception('(precisa ser implementado)')
        return rowcount > 0

    @staticmethod
    def delete(carro_id):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM carros WHERE oid_carro = %s"
        valores = (carro_id,)
        cursor.execute(sql, valores)
        conn.commit()
        rowcount = cursor.rowcount
        cursor.close()
        conn.close()
        # raise Exception('(precisa ser implementado)')
        return rowcount > 0