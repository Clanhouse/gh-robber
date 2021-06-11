from backend.app.api.ver_1_0 import users_api
from backend.app.models import User, GithubUser


@users_api.route("/users/")
def get_users():
    users = [user.email for user in User.query.all()]
    return {"users": users}


@users_api.route("/github-users/")
def get_github_users():
    github_users = [github_user.username for github_user in GithubUser.query.all()]
    return {"github_users": github_users}
