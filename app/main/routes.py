from flask import render_template
from flask_login import login_required, current_user
from . import main_bp

@main_bp.route('/')
def index():
    return render_template('main/index.html', title='Főoldal')

@main_bp.route('/dashboard')
@login_required # Ezt az oldalt csak bejelentkezve lehet látni
def dashboard():
    return render_template('main/index.html', title='Vezérlőpult', is_dashboard=True)