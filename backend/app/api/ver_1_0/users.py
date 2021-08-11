from backend.app.api.ver_1_0 import users_api
from backend.app.models import User, GithubUser, GithubUserInfo, GithubUserInfoSchema, info_schema
from flask import jsonify, request

@users_api.route("/users/")
def get_users():
    users = [user.email for user in User.query.all()]
    return {"users": users}


@users_api.route("/github-users/")
def get_github_users():
    github_users = [github_user.username for github_user in GithubUser.query.all()]
    return {"github_users": github_users}

@users_api.route("/search/", methods=['GET'])
def users_info():
    query = GithubUserInfo.query
    schema_args = GithubUserInfo.get_args(request.args.get("fields"))
    query = GithubUserInfo.apply_order(query, request.args.get("sort"))
    users = query.all()
    user_schema = GithubUserInfoSchema(**schema_args)

    return jsonify({
        "success": True,
        "data": user_schema.dump(users),
        "numbers_of_records": len(users)
    })
