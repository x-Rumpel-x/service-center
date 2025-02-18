from mysql.connector import Error
from ..utils import get_db_connection


def create_clients_table():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(50),
                    surname VARCHAR(50),
                    middle_name VARCHAR(50),
                    phone_number VARCHAR(50),
                    telegram VARCHAR(50)                                             
                );
            """)
            connection.commit()
        except Error as e:
            print(f"Ошибка: {e}")
        finally:
            cursor.close()
            connection.close()
