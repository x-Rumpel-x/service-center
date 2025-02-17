import os

from mysql.connector import connect, Error


def get_db_connection():
    try:
        connection = connect(
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT', 3306)),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_DATABASE'),
        )
        return connection
    except Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None
