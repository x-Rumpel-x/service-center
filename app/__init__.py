import os

from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv

from app.models.staff import get_staff_by_id

from app.migration.make_migrations import make_migrations

# Инициализация LoginManager
login_manager = LoginManager()
login_manager.login_view = 'admin.login'


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY', 'your_secret_key')

    load_dotenv(dotenv_path='.env')

    # Инициализация расширений
    login_manager.init_app(app)

    # Привязка функции загрузки пользователя к LoginManager
    login_manager.user_loader(get_staff_by_id)

    # Регистрация блюпринтов
    from .routes.admin_routes import admin_bp
    app.register_blueprint(admin_bp)

    make_migrations()

    return app
