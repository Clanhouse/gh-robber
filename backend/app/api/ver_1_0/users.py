from webargs.flaskparser import use_args
from backend.app.api.ver_1_0 import users_api
from backend.app.models import User, GithubUser, GithubUserInfo, GithubUserInfoSchema, info_schema
from flask import jsonify, request, make_response


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
    query = GithubUserInfo.apply_filter(query, request.args)
    users = query.all()
    user_schema = GithubUserInfoSchema(**schema_args)

    return jsonify({
        "success": True,
        "data": user_schema.dump(users),
        "numbers_of_records": len(users)
    })

# TODO needs validation - by marshmallow
@users_api.route("/github-users-post/", methods=['POST'])
def new_user_info():
    data = request.get_json()
    user_info_schema = info_schema
    user_info = user_info_schema.load(data)
    # TODO there has to be a way to do this automatically..
    user_info_obj = GithubUserInfo(user_info["id"], user_info["username"], user_info["language"], user_info["date"], user_info["stars"], user_info["number_of_repositories"])
    result = user_info_schema.dump(user_info_obj.create())

    return make_response(jsonify({"added-user-info": result}), 200)


@users_api.route('/users', methods=['POST'])
@use_args(info_schema)
def create_author(args: dict):
    github_user = GithubUserInfo(**args)

    db.session.add(github_user)
    db.session.commit()

    return jsonify({'data': info_schema.dump(github_user)}),  200

@users_api.route('/users/<int:github_user_id>', methods=['PUT'])
@use_args(info_schema)
def update_author(github_user_id: int):
    github_user = GithubUserInfo.query.get_or_404(github_user_id, description=f'Github user with id {github_user_id} not found')

    github_user.username = args['username']
    github_user.language = args['language']
    github_user.date = args['date']
    github_user.stars = args['star']
    github_user.number_of_repositories = args['number_of_repositories']

    db.session.commit()

    return jsonify({'data': info_schema.dump(github_user)})

# @users_api.route('/users/<int:user_id>', methods=['DELETE'])
# def delete_user_info(github_user_id: int):
#     github_user = GithubUserInfo.query.get_or_404(github_user_id, description=f'Github user with id {github_user_id} not found')
#     db.session.delete(github_user)
#
#     db.session.commit()
#
#     return jsonify({'data': f'Github user with id {github_user_id} has been deleted'})