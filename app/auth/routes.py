from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from . import auth_bp
from .forms import LoginForm, RegistrationForm
from ..models import User
from ..extensions import db

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        # Ellenőrizzük, létezik-e már az email vagy a felhasználónév
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Ez az email cím már foglalt.', 'danger')
            return redirect(url_for('auth.register'))
            
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Sikeres regisztráció! Most már bejelentkezhetsz.', 'success')
        return redirect(url_for('auth.login'))
        
    return render_template('auth/register.html', title='Regisztráció', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
        
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and user.check_password(form.password.data):
            login_user(user)
            # Ha egy védett oldalról irányították ide, visszadobjuk oda bejelentkezés után
            next_page = request.args.get('next')
            flash('Sikeres bejelentkezés!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Hibás email cím vagy jelszó.', 'danger')
            
    return render_template('auth/login.html', title='Bejelentkezés', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Sikeresen kijelentkeztél.', 'info')
    return redirect(url_for('main.index'))