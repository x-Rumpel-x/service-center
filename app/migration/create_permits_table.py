from mysql.connector import Error
from ..utils import get_db_connection


def create_permits_table():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE permits (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    ip INT UNSIGNED NOT NULL UNIQUE
                );
            """)
            connection.commit()
        except Error as e:
            print(f"Ошибка: {e}")
        finally:
            cursor.close()
            connection.close()

