from mysql.connector import Error
from ..utils import get_db_connection


def create_orders_table():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS orders (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    order_number INT NOT NULL,
                    order_office INT NOT NULL,
                    client INT NOT NULL,
                    brief VARCHAR(255) NOT NULL,
                    description TEXT NOT NULL,
                    status INT NOT NULL,
                    FOREIGN KEY (status) REFERENCES order_status (id)                                          
                );
            """)
            connection.commit()
        except Error as e:
            print(f"Ошибка: {e}")
        finally:
            cursor.close()
            connection.close()