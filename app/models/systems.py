import locale

from app.utils import get_db_connection
from datetime import datetime
from flask import jsonify
from pytz import timezone


def get_remote_ip(user_ip):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT INET_NTOA(ip) FROM permits WHERE ip = %s', (user_ip,))
    ip = cursor.fetchone()


locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

weekdays_ru = {
    0: 'Пн', 1: 'Вт', 2: 'Ср', 3: 'Чт', 4: 'Пт', 5: 'Сб', 6: 'Вс'
}


def get_time():
    """
        Функция для получения текущей даты и времени.
    """
    now = datetime.now()  # Можно заменить на datetime.now(timezone('Europe/Moscow'))
    return jsonify(
        time=now.strftime("%H:%M"),
        date=now.strftime("%d.%m"),
        weekday=weekdays_ru[now.weekday()],
        datetime_iso=now.isoformat()
    )
