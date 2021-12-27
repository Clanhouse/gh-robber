from flask_admin.contrib import sqla
From backend.app import db
From backend.app.models import User, GithubUserInfo

class UserAccountView(sqla.ModelView):
    list_template = 'admin/model/list_users.html'
    column_searchable_list = ('id','username', 'email', 'creation_date')
    column_list = ('id', 'username', 'email', 'creation_date')
    column_display_pk = True
    column_default_sort = "id"
    form_columns = ['username', 'email', 'creation_date']
    form_excluded_columns = ['password']

class GHUsersInfoView(sqla.ModelView):
    column_searchable_list = ('username', 'repository', 'languages', 'date','number_of_repositories')
    column_list = ('username', 'repository', 'languages', 'date', 'number_of_repositories', 'stars')
    column_display_pk = False
    column_default_sort = "username"
    form_columns = ['username', 'repository', 'languages', 'date', 'number_of_repositories', 'stars']
