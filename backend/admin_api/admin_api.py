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


# To do: Change this route when integrating other GH Robber components.
# If you just want to test GHRobber Admin API for functionality and etc, keep this the same. Run module on it's own.

@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'


admin = Admin(app, base_template='admin/custom_base.html', index_view=AdminIndexView(name='Dashboard', template='dashboard.html'), template_mode='bootstrap4')

from .admin_api import admin_models
from ..admin_models import UserAccountView, User, GHUsersInfoView, GithubUserInfo, AuthView, DocsView
    
admin.add_view(DocsView(name="Documentation", endpoint='/docs'))
admin.add_view(UserAccountView(User, db.session, name="User Management"))
admin.add_view(GHUsersInfoView(GithubUserInfo, db.session, name="Github Management"))
admin.add_view(GHUsersAPIView(name="API", endpoint="/api/v1/users"))
admin.add_view(AuthView(name="Authentication", endpoint='/auth'))


if __name__ == '__main__':

    # the test database
    db.create_all()
    
    app.run(debug=True)
