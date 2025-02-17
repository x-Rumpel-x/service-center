from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, login_user, current_user
from passlib.hash import bcrypt
from datetime import datetime

from ..models.staff.staff import get_staff_by_username

admin_bp = Blueprint('admin', __name__, template_folder='../templates/admin')


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
        Маршрут для авторизации пользователя.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        staff = get_staff_by_username(username)

        if staff and bcrypt.verify(password, staff.password):
            login_user(staff)
            flash('Вы успешно вошли в систему!', 'success')
            return redirect(url_for('admin.dashboard'))
    else:
        flash('Неверное имя пользователя или пароль.', 'danger')
    return render_template('login.html')


@admin_bp.route('/time')
def get_time():
    now = datetime.now().strftime("%H:%M")
    return jsonify(time=now)


@admin_bp.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html')
