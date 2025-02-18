from mysql.connector import Error
from ..utils import get_db_connection


def create_stats_table():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS stats_table (
                    id INT AUTO_INCREMENT PRIMARY KEY,
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
