from mysql.connector import Error
from ..utils import get_db_connection


def create_notifications_table():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notifications (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    notification TEXT NOT NULL,
                    to_user TEXT NOT NULL,
                    check_it TEXT NOT NULL                                     
                );
            """)
            connection.commit()
        except Error as e:
            print(f"Ошибка: {e}")
        finally:
            cursor.close()
            connection.close()