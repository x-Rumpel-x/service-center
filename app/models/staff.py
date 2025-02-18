from flask_login import UserMixin
from app.utils import get_db_connection


class Staff(UserMixin):
    def __init__(self, id, name, surname, middle_name, password, role, status, status_comment, telegram, profit,
                 order_completed, made_sales, salary):
        self.id = id
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.password = password
        self.role = role
        self.status = status
        self.status_comment = status_comment
        self.telegram = telegram
        self.profit = profit
        self.order_completed = order_completed
        self.made_sales = made_sales
        self.salary = salary


def get_staff_by_id(staff_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM staff WHERE id = %s', (staff_id,))
    staff = cursor.fetchone()
    if staff:
        return Staff(staff[0], staff[1], staff[2], staff[3], staff[4], staff[5], staff[6], staff[7], staff[8], staff[9],
                     staff[10], staff[11], staff[12])
    return None


def get_staff_by_username(username):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM staff WHERE name = %s', (username,))
    staff = cursor.fetchone()
    if staff:
        return Staff(staff[0], staff[1], staff[2], staff[3], staff[4], staff[5], staff[6], staff[7], staff[8], staff[9],
                     staff[10], staff[11], staff[12])
    return None
