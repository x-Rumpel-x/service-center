from mysql.connector import Error
from ..utils import get_db_connection


def create_profit_table():
    connection = get_db_connection()
    if connection:
        cursor = None
        try:
            cursor = connection.cursor()

            # Создаем таблицу с улучшенной структурой
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS profit (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    amount INT NOT NULL DEFAULT 0,
                    date DATE,
                    time TIME
                );
            """)

            # Проверяем существующие записи
            cursor.execute("SELECT COUNT(*) FROM profit")
            count = cursor.fetchone()[0]

            # Если таблица пустая - добавляем дефолтную запись
            if count == 0:
                cursor.execute(
                    "INSERT INTO profit (amount, date, time) VALUES (%s, CURDATE(), CURTIME())",
                    (1000,)
                )

            connection.commit()

        except Error as e:
            print(f"Database error: {e}")
            connection.rollback()
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()