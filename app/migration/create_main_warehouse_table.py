from mysql.connector import Error
from ..utils import get_db_connection


def create_main_warehouse_table():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS main_warehouse (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    item_code INT,
                    item_name VARCHAR(255) UNIQUE,
                    count INT,
                    office_id INT
                );
            """)
            connection.commit()
        except Error as e:
            print(f"Ошибка: {e}")
        finally:
            cursor.close()
            connection.close()
