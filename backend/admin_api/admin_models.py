from flask_admin.contrib import sqla
from app import db

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
