from .create_staff_status_table import create_staff_status_table
from .create_staff_table import create_staff_table, create_root_user
from .create_stats_table import create_stats_table
from .create_permits_table import create_permits_table


def make_migrations():
    create_staff_status_table()
    create_staff_table()
    create_stats_table()
    create_permits_table()

    create_root_user()
    return print(f"Миграции выполнены успешно")
