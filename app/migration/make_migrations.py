from .create_staff_status_table import create_staff_status_table
from .create_staff_table import create_staff_table, create_root_user
from .create_stats_table import create_stats_table
from .create_permits_table import create_permits_table
from .create_warehouse_table import create_warehouse_table
from .create_main_warehouse_table import create_main_warehouse_table
from .create_offices_table import create_offices_table
from .create_order_status_table import create_order_status_table
from .create_orders_table import create_orders_table
from .create_clients_table import create_clients_table
from .create_notifications_table import create_notifications_table


def make_migrations():
    create_staff_status_table()
    create_staff_table()
    create_stats_table()
    create_permits_table()
    create_warehouse_table()
    create_main_warehouse_table()
    create_offices_table()
    create_order_status_table()
    create_orders_table()
    create_clients_table()
    create_notifications_table()

    create_root_user()
    return print(f"Миграции выполнены успешно")
