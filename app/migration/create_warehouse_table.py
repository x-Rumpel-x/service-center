from mysql.connector import Error
from ..utils import get_db_connection


def create_warehouse_table():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS warehouse (
                    office_id INT,
                    item_code INT,
                    item_name VARCHAR(255) UNIQUE,
                    count INT                                              
                );
            """)
            connection.commit()
        except Error as e:
            print(f"Ошибка: {e}")
        finally:
            cursor.close()
            connection.close()