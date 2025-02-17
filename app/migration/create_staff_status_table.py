from mysql.connector import Error
from ..utils import get_db_connection


def create_staff_status_table():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS staff_status (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    status VARCHAR(11)
                );
            """)
            connection.commit()
            cursor.execute("""
                INSERT INTO `staff_status` (`status`) 
                VALUES 
                    ('Работает'),
                    ('Отпуск'),
                    ('Больничный'),
                    ('Уволен');
            """)
            connection.commit()
        except Error as e:
            print(f"Ошибка: {e}")
        finally:
            cursor.close()
            connection.close()

