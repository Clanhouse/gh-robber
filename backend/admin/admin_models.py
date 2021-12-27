from flask_admin.contrib import sqla
from config import db

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

class GithubUserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    repository = db.Column(db.String(255), nullable=False)
    languages = db.Column(db.JSON, nullable=False)
    date = db.Column(db.Date(), nullable=False)
    number_of_repositories = db.Column(db.Integer, nullable=False)
    stars = db.Column(db.Integer, nullable=False)


class UserAccountView(sqla.ModelView):
    list_template = 'admin/model/list_users.html'
    column_searchable_list = ('id','name', 'email')
    column_list = ('id','name', 'email')
    column_display_pk = True
    column_default_sort = "name"
    form_columns = ['name', 'email']
    form_excluded_columns = ['password']

class GHUsersInfoView(sqla.ModelView):
    column_searchable_list = ('id','username', 'repository', 'languages', 'date','number_of_repositories')
    column_list = ('id','username', 'repository', 'languages', 'date', 'number_of_repositories', 'stars')
    column_display_pk = True
    column_default_sort = "stars"
    form_columns = ['username', 'repository', 'languages', 'date', 'number_of_repositories', 'stars']
