from config.conexao import get_connection
class CarroModel:
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
        SELECT
            oid_carro, nom_carro, nom_marca, num_ano_fabricacao, num_ano_modelo, nom_cor, nom_combustivel, num_placa, dat_criacao, dat_alteracao
        FROM carro
        """)
        result = cursor.fetchone()
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
        FROM carro
        WHERE
            oid_carro = %s""", (carro_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def insert(dados):
        # conn = get_connection()
        # cursor = conn.cursor()
        # sql = "INSERT INTO series (titulo, ano, categoria, sinopse, faixa_etaria, pais, idioma) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        # valores = (dados.get('titulo'), dados.get('ano'), dados.get('categoria'), dados.get('sinopse'), dados.get('faixa_etaria'), dados.get('pais'), dados.get('idioma'))
        # cursor.execute(sql, valores)
        # conn.commit()
        # last_id = cursor.lastrowid
        # cursor.close()
        # conn.close()
        raise Exception('(precisa ser implementado)')
        return last_id

    @staticmethod
    def update(serie_id, dados):
        # conn = get_connection()
        # cursor = conn.cursor()
        # sql = "UPDATE series set titulo=%s, ano=%s, categoria=%s, sinopse=%s, faixa_etaria=%s, pais=%s, idioma=%s WHERE id=%s"
        # valores = (dados.get('titulo'), dados.get('ano'), dados.get('categoria'), dados.get('sinopse'), dados.get('faixa_etaria'), dados.get('pais'), dados.get('idioma'), serie_id)
        # cursor.execute(sql, valores)
        # conn.commit()
        # rowcount = cursor.rowcount
        # cursor.close()
        # conn.close()
        raise Exception('(precisa ser implementado)')
        return rowcount > 0

    @staticmethod
    def delete(serie_id):
        # conn = get_connection()
        # cursor = conn.cursor()
        # sql = "DELETE FROM series WHERE id = %s"
        # valores = (serie_id,)
        # cursor.execute(sql, valores)
        # conn.commit()
        # rowcount = cursor.rowcount
        # cursor.close()
        # conn.close()
        raise Exception('(precisa ser implementado)')
        return rowcount > 0