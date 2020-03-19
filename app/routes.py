# -*- coding: utf-8 -*-
from app import app
from flask import render_template
from app.forms import LoginForm, AssetForm
from app.models import Assets
# from wtforms.ext.sqlalchemy.orm import model_form
# from myapp.models import User
#


@app.route('/')
@app.route('/index')
def index():

    assets = Assets.query.all()
    user = {'username': 'Travis'}
    return render_template('index.html', title='Home', user=user, assets=assets)


@app.route('/Admin')
def hello():
    return "Hello Admin"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@app.route('/Asset')
def asset():
    # form = model_form(Assets)
    form = AssetForm()
    return render_template('assets.html', title='Asset Entry', form=form)

