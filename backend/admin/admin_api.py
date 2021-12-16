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
from config import db, app

# To do: Change this route when integrating other GH Robber components
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

admin = Admin(app, base_template='admin/custom_base.html', index_view=AdminIndexView(name='Dashboard', template='dashboard.html'), template_mode='bootstrap4')

from admin_models import Role, User, GithubUserInfo,UserAccountView, GHUsersInfoView

class GHUsersAPIView(BaseView):
    @expose('/', methods=('GET','POST'))
    def index(self):
        return self.render('api_users_index.html')


    @expose_plugview('/users')
    class UsersAPI(MethodView):
        def get(self, cls):
            return cls.render('method_request.html', request=request, name="Users")

        def post(self, cls):
            return cls.render('method_request.html', request=request, name="Users")


class AuthView(BaseView):
    @expose('/', methods=('GET','POST'))
    def index(self):
        return self.render('api_auth_index.html')

    @expose_plugview('/login')
    class UserLogin(MethodView):
        def get(self, cls):
            return cls.render('login.html', request=request, name="Login")

        def post(self, cls):
            return cls.render('login.html', request=request, name="Login")

    @expose_plugview('/register')
    class UserRegistration(MethodView):
        def get(self, cls):
            return cls.render('register_form.html', request=request, name="Registration")

        def post(self, cls):
            return cls.render('register_form.html', request=request, name="Registration")

    @expose_plugview('/me')
    class CurrentUser(MethodView):
        def post(self, cls):
            return cls.render('method_request.html', request=request, name="My Profile")
        def get(self, cls):
            return cls.render('method_request.html', request=request, name="My Profile")


    @expose_plugview('/update/password')
    class UpdateUserPassword(MethodView):
        def post(self, cls):
            return cls.render('method_request.html', request=request, name="Update Password")

        def get(self, cls):
            return cls.render('method_request.html', request=request, name="Update Password")


    @expose_plugview('/update/data')
    class UpdateUserData(MethodView):
        def post(self, cls):
            return cls.render('method_request.html', request=request, name="Update Information")

        def get(self, cls):
            return cls.render('method_request.html', request=request, name="Update Information")

class DocsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('documentation.html')


admin.add_view(UserAccountView(User, db.session, name="User Management"))
admin.add_view(GHUsersInfoView(GithubUserInfo, db.session, name="Github Management"))

admin.add_view(GHUsersAPIView(name="API", endpoint="/api/v1/users"))

admin.add_view(AuthView(name="Authentication", endpoint='/auth'))
admin.add_view(DocsView(name="Documentation", endpoint='/docs'))

#admin.add_view(RoleView(Role, db.session, category="Role"))


if __name__ == '__main__':

    db.create_all()

    app.run(debug=True)
