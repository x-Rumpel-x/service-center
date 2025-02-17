from .create_staff_status_table import create_staff_status_table
from .create_staff_table import create_staff_table, create_root_user


def make_migrations():
    create_staff_status_table()
    create_staff_table()

    create_root_user()
    return print(f"Миграции выполнены успешно")
