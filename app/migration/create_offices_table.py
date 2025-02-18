from mysql.connector import Error
from ..utils import get_db_connection


def create_offices_table():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS offices (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    office_id INT UNIQUE,
                    postal_code INT,
                    city VARCHAR(255),
                    street VARCHAR(255),
                    house VARCHAR(255),
                    office VARCHAR(255),
                    profit INT DEFAULT 0,
                    order_completed INT DEFAULT 0,
                    made_sales INT DEFAULT 0                          
                );
            """)
            connection.commit()
        except Error as e:
            print(f"Ошибка: {e}")
        finally:
            cursor.close()
            connection.close()