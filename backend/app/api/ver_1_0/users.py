from flask import jsonify, request, make_response
from webargs.flaskparser import use_args
from backend.app import db
from backend.app.api.ver_1_0 import users_api
from backend.app.models import GithubUserInfo, GithubUserInfoSchema, info_schema
from backend.utils import validate_json_content_type


@users_api.route("/users", methods=['GET'])
def get_users_info():
    query = GithubUserInfo.query
    schema_args = GithubUserInfo.get_args(request.args.get("fields"))
    query = GithubUserInfo.apply_order(query, request.args.get("sort"))
    query = GithubUserInfo.apply_filter(query)
    items, pagination = GithubUserInfo.get_pagination(query)
    users = GithubUserInfoSchema(**schema_args).dump(items)

    return jsonify({
        "data": users,
        "numbers_of_records": len(users),
        "pagination": pagination
    })


@users_api.route('/users/<int:github_user_id>', methods=['GET'])
def get_user_info(github_user_id: int):
    github_user = GithubUserInfo.query.get_or_404(github_user_id, description=f'Github user with id {github_user_id} not found')
    return jsonify({
        'data': info_schema.dump(github_user)
    })


@users_api.route('/users', methods=['POST'])
@validate_json_content_type
@use_args(info_schema, error_status_code=400)
def create_user_info(args: dict):
    github_user = GithubUserInfo(**args)

    db.session.add(github_user)
    db.session.commit()

    return jsonify({'data': info_schema.dump(github_user)}),  201


@users_api.route('/users/<int:github_user_id>', methods=['PUT'])
@validate_json_content_type
@use_args(info_schema, error_status_code=400)
def update_user_info(args: dict, github_user_id: int):
    github_user = GithubUserInfo.query.get_or_404(github_user_id, description=f'Github user with id {github_user_id} not found')

    github_user.username = args['username']
    github_user.language = args['language']
    github_user.date = args['date']
    github_user.stars = args['star']
    github_user.number_of_repositories = args['number_of_repositories']

    db.session.commit()

    return jsonify({'data': info_schema.dump(github_user)})


@users_api.route('/users/<int:github_user_id>', methods=['DELETE'])
def delete_user_info(github_user_id: int):
    github_user = GithubUserInfo.query.get_or_404(github_user_id, description=f'Github user with id {github_user_id} not found')

    db.session.delete(github_user)
    db.session.commit()

    return jsonify({'data': f'Github user with id {github_user_id} has been deleted'})