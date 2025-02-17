from mysql.connector import Error
from ..utils import get_db_connection
from passlib.hash import bcrypt


def create_staff_table():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS staff (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(50),
                        surname VARCHAR(50),
                        middle_name VARCHAR(50),
                        password VARCHAR(255),
                        role INT NOT NULL DEFAULT 1,
                        status INT NOT NULL DEFAULT 1,
                        FOREIGN KEY(status) REFERENCES staff_status(id),
                        status_comment TEXT NOT NULL DEFAULT '',
                        telegram VARCHAR(255),
                        profit INT NOT NULL DEFAULT 0,
                        order_completed INT NOT NULL DEFAULT 0,
                        made_sales INT NOT NULL DEFAULT 0,
                        salary INT NOT NULL DEFAULT 0
                    );
                """)
            connection.commit()
        except Error as e:
            print(f"Ошибка: {e}")
        finally:
            cursor.close()
            connection.close()


def create_root_user():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()

            # Проверяем, существует ли уже пользователь с ролью 4 (root)
            cursor.execute("SELECT id FROM staff WHERE role = 4 LIMIT 1")
            existing_user = cursor.fetchone()

            # Если такого пользователя нет, создаем нового
            if not existing_user:
                # Хеширование пароля "root"
                hashed_password = bcrypt.hash('root')

                # Вставляем пользователя в таблицу
                cursor.execute(
                    """INSERT INTO staff (name, surname, middle_name, password, role) VALUES (%s, %s, %s, %s, %s)""",
                    ("Root", "Root", "Root", hashed_password, 4))

                connection.commit()

            else:
                print("Пользователи уже существуют, функция не будет выполняться повторно.")

        except Exception as e:
            print(f"Ошибка при создании пользователей: {e}")

        finally:
            # Закрытие курсора и соединения
            if cursor:
                cursor.close()
            if connection:
                connection.close()

