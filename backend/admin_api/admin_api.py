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

# TO DO - delete all config settings nelow, except flask_admin_swatch
app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'lux'
app.config['SECRET_KEY'] = '123456790'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admin_api.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


admin = Admin(app, base_template='admin/custom_base.html', index_view=AdminIndexView(name='Dashboard', template='dashboard.html'), template_mode='bootstrap4')

from admin_models import UserAccountView, GHUsersInfoView
from app.models import User, GithubUserInfo

admin.add_view(UserAccountView(User, db.session, name="User Management"))
admin.add_view(GHUsersInfoView(GithubUserInfo, db.session, name="Github Management"))


if __name__ == '__main__':

    # the test database - to be deleted
    db.create_all()
    
    app.run(debug=True)
