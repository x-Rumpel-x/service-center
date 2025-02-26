from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, login_user, logout_user
from passlib.hash import bcrypt

from app.models.staff import get_staff_by_username
from app.models.systems import get_remote_ip
from app.models.systems import get_time
from app.migration.make_migrations import make_migrations

admin_bp = Blueprint('admin', __name__, template_folder='../templates/admin')
admin_bp.route('/time')(get_time)


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
        Маршрут для авторизации пользователя.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_ip = request.remote_addr

        staff = get_staff_by_username(username)
        ip_allowed = (get_remote_ip(user_ip) == user_ip)

        if staff and bcrypt.verify(password, staff.password):
            if ip_allowed or staff.role == 4:
                login_user(staff)
                flash('Вы успешно вошли в систему!', 'success')
                return redirect(url_for('admin.dashboard'))
    else:
        flash('Неверное имя пользователя или пароль.', 'danger')
    return render_template('login.html')


@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))


@admin_bp.route('/')
@login_required
def dashboard():
    """
        Маршрут для дашборда.
    """
    return render_template('dashboard.html')


@admin_bp.route('/orders', methods=['GET', 'POST'])
@login_required
def orders():
    """
        Маршрут для заказов (ремонтов).
    """
    return render_template('orders.html')


@admin_bp.route('/warehouse', methods=['GET', 'POST'])
@login_required
def warehouse():
    """
        Маршрут для локального склада.
    """
    return render_template('warehouse.html')


@admin_bp.route('/main-warehouse', methods=['GET', 'POST'])
@login_required
def main_warehouse():
    """
        Маршрут для общего склада.
    """
    return render_template('main_warehouse.html')


@admin_bp.route('/staff', methods=['GET', 'POST'])
@login_required
def staff():
    """
        Маршрут для управления персоналом.
    """
    return render_template('staff_manage.html')


@admin_bp.route('/office', methods=['GET', 'POST'])
@login_required
def office():
    """
        Маршрут для управления офисами.
    """
    return render_template('office_manage.html')


@admin_bp.route('/migrations')
@login_required
def migrations():
    """
        Маршрут для выполнения миграций.
    """
    make_migrations()
