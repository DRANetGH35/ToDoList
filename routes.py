
from flask import render_template, redirect, request, flash
from flask_login import current_user, logout_user, login_user
from werkzeug.security import generate_password_hash

from forms import LoginForm, CreateAccountForm
from extensions import db
from models import User
from app import create_app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html', current_user=current_user)

@app.route('/log_in')
def log_in():
    form = LoginForm()
    return render_template('log_in.html', form=form)

@app.route('/log_out')
def log_out():
    logout_user()
    return redirect(request.referrer)

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    form = CreateAccountForm()
    if request.method == 'POST':
        entered_username = request.form.get('username')
        entered_password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if entered_password != confirm_password:
            flash('passwords must match', 'error')
        else:
            new_user = User(name=entered_username,
                        password=generate_password_hash(password=entered_password, method='pbkdf2:sha256', salt_length=8),
                        is_admin=False)
            db.session.add(new_user)
            db.session.commit()
        return render_template('create_account.html', form=form)
    return render_template('create_account.html', form=form)