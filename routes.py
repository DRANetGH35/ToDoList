
from flask import render_template, redirect, request
from flask_login import current_user, logout_user

from forms import LoginForm
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