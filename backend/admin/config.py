from flask import Flask, redirect, request
from flask.views import MethodView
import flask_wtf
import wtforms
from flask_sqlalchemy import SQLAlchemy
import flask_admin
from flask_admin.contrib import sqla
from flask_admin import Admin
from flask_admin.base import BaseView, expose, expose_plugview, AdminIndexView
import os
from flask_admin.menu import MenuCategory, MenuView, MenuLink, SubMenuCategory
from flask.views import MethodView
from flask import render_template

app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'lux'
app.config['SECRET_KEY'] = '123456790'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin_api.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
