from mysql.connector import Error
from ..utils import get_db_connection


def create_profit_table():
    connection = get_db_connection()
    if connection:
        cursor = None
        try:
            cursor = connection.cursor()

            # Создаем таблицу для временных рядов
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS profit_metrics (
                    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    amount DECIMAL(1000,2) NOT NULL,
                    category VARCHAR(50),
                    source VARCHAR(50),
                    PRIMARY KEY (time)
                );
            """)

            # Оптимизация для частых запросов Grafana
            cursor.execute("""
                ALTER TABLE profit_metrics 
                ADD INDEX time_index (time)
            """)

            # Проверка и инициализация тестовых данных
            cursor.execute("SELECT COUNT(*) FROM profit_metrics")
            if cursor.fetchone()[0] == 0:
                cursor.execute("""
                    INSERT INTO profit_metrics (amount, category, source)
                    VALUES (%s, %s, %s)
                """, (1000.00, 'initial', 'system'))

            connection.commit()

        except Error as e:
            print(f"Grafana DB Error: {e}")
            connection.rollback()
        finally:
            if cursor: cursor.close()
            if connection: connection.close()