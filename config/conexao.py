import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="usr_app_dev_api",
        password="123456",
        database="dev_api"
    )
