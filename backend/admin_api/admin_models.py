from flask import Flask, redirect, request
from flask.views import MethodView
import flask_wtf
import wtforms
from flask_sqlalchemy import SQLAlchemy
import flask_admin
from flask_admin.contrib import sqla
from flask_admin import Admin
from flask_admin.base import BaseView, expose, expose_plugview, AdminIndexView
from flask_admin.menu import MenuCategory, MenuView, MenuLink, SubMenuCategory
from flask.views import MethodView
from flask import render_template



class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    title = db.Column(db.String(255))
    desc = db.Column(db.String(50))

    def __unicode__(self):
        return self.desc

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    desc = db.Column(db.String(50))
    def __unicode__(self):
        return self.desc

class GithubUserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    repository = db.Column(db.String(255), nullable=False)
    languages = db.Column(db.JSON, nullable=False)
    date = db.Column(db.Date(), nullable=False)
    number_of_repositories = db.Column(db.Integer, nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String(50))

    def __unicode__(self):
        return self.desc


class UserAccountView(sqla.ModelView):
    list_template = 'templates/db_views/list_users.html'
    create_template = 'templates/db_views/create_users.html'
    edit_template = 'templates/db_views/edit_users.html'
    column_searchable_list = ('id','name', 'email')
    column_list = ('id','name', 'email', 'password')
    column_display_pk = True
    column_default_sort = "name"
    form_columns = ['name', 'email', 'password']

class GHUsersInfoView(sqla.ModelView):
    list_template = 'templates/db_views/list_users.html'
    create_template = 'templates/db_views/create_users.html'
    edit_template = 'templates/db_views/edit_users.html'
    column_searchable_list = ('id','username', 'repository', 'languages', 'date','number_of_repositories')
    column_list = ('id','username', 'repository', 'languages', 'date', 'number_of_repositories', 'stars')
    column_display_pk = True
    column_default_sort = "stars"
    form_columns = ['username', 'repository', 'languages', 'date', 'number_of_repositories', 'stars']

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
