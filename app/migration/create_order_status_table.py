from mysql.connector import Error
from ..utils import get_db_connection


def create_order_status_table():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS order_status (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    status VARCHAR(20) UNIQUE NOT NULL
                );
            """)

            # Вставляем значения, если таблица пустая
            cursor.execute("SELECT COUNT(*) FROM order_status")
            count = cursor.fetchone()[0]

            if count == 0:
                cursor.executemany(
                    "INSERT INTO order_status (status) VALUES (%s)",
                    [("Принят",), ("В работе",), ("Завершен",), ("Отменен",)]
                )

            connection.commit()
        except Error as e:
            print(f"Ошибка: {e}")
        finally:
            cursor.close()
            connection.close()
