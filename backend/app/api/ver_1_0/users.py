from app import db
from flask import jsonify
from flask import request
from webargs.flaskparser import use_args
from app.api.ver_1_0 import users_api
from app.models import GithubUserInfo
from app.models import GithubUserInfoSchema
from app.models import info_schema
from app.utils import token_required
from app.utils import validate_json_content_type


@users_api.route("/users", methods=["GET"])
def get_users_info():
    query = GithubUserInfo.query
    schema_args = GithubUserInfo.get_args(request.args.get("fields"))
    query = GithubUserInfo.apply_order(query, request.args.get("sort"))
    query = GithubUserInfo.apply_filter(query)
    items, pagination = GithubUserInfo.get_pagination(query)
    users = GithubUserInfoSchema(**schema_args).dump(items)

    return jsonify(
        {"data": users, "numbers_of_records": len(users), "pagination": pagination}
    )


@users_api.route("/users/<int:github_user_id>", methods=["GET"])
def get_user_info(github_user_id: int):
    github_user = GithubUserInfo.query.get_or_404(
        github_user_id, description=f"Github user with id {github_user_id} not found"
    )
    return jsonify({"success": True, "data": info_schema.dump(github_user)})


@users_api.route("/users", methods=["POST"])
@token_required
@validate_json_content_type
@use_args(info_schema, error_status_code=400)
def create_user_info(user_id: int, args: dict):
    github_user = GithubUserInfo(**args)

    db.session.add(github_user)
    db.session.commit()

    return jsonify({"success": True, "data": info_schema.dump(github_user)}), 201


@users_api.route("/users/<int:github_user_id>", methods=["PUT"])
@token_required
@validate_json_content_type
@use_args(info_schema, error_status_code=400)
def update_user_info(user_id: int, args: dict, github_user_id: int):
    github_user = GithubUserInfo.query.get_or_404(
        github_user_id, description=f"Github user with id {github_user_id} not found"
    )

    github_user.username = args["username"]
    github_user.language = args["language"]
    github_user.date = args["date"]
    github_user.stars = args["stars"]
    github_user.number_of_repositories = args["number_of_repositories"]

    db.session.commit()

    return jsonify({"success": True, "data": info_schema.dump(github_user)})


@users_api.route("/users/<int:github_user_id>", methods=["DELETE"])
@token_required
def delete_user_info(user_id: int, github_user_id: int):
    github_user = GithubUserInfo.query.get_or_404(
        github_user_id, description=f"Github user with id {github_user_id} not found"
    )

    db.session.delete(github_user)
    db.session.commit()

    return jsonify({"data": f"Github user with id {github_user_id} has been deleted"})


@users_api.route("/index/<string:github_user_username>", methods=["GET"])
@token_required
def get_user_from_github(github_user_username: str):

    try:
        github_user = search_for_user(github_user_username)

        return jsonify({"data": f"{github_user}"})
    except Exception:
        return jsonify({"data": f"user {github_user_username} has not found"})
