import re
import jwt
from typing import Tuple
from datetime import datetime
from datetime import timedelta
import sqlalchemy.orm
from flask import request
from flask import url_for
from flask import current_app
from flask_sqlalchemy import BaseQuery
from marshmallow import Schema
from marshmallow import fields
from marshmallow import validate
from marshmallow import validates
from marshmallow import ValidationError
from sqlalchemy import distinct, or_
from sqlalchemy import and_
from sqlalchemy import not_
from sqlalchemy import Table, Column, Integer, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.sql.expression import BinaryExpression
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from . import db


class GHReposAndUsers(db.Model):
    __tablename__ = "gh_repos_and_gh_users"
    id = db.Column(Integer, primary_key=True)
    github_user_id = db.Column(Integer, ForeignKey("github_users_info.id"))
    github_repository_id = db.Column(Integer, ForeignKey("github_repositories.id"))


class GithubRepositories(db.Model):
    __tablename__ = "github_repositories"
    id = db.Column(db.Integer, primary_key=True)
    reponame = db.Column(db.String(70), nullable=False)
    languages = db.Column(db.JSON, nullable=False)
    last_update = db.Column(db.Date(), nullable=False)
    topics = db.Column(db.JSON, nullable=True)
    last_commit_date = db.Column(db.Date(), nullable=True)
    stars = db.Column(db.Integer, nullable=False)
    has_sourced_users = db.Column(db.Boolean)
    contributors = db.relationship(
        "GithubUserInfo",
        secondary="gh_repos_and_gh_users",
        back_populates="repositories",
    )

    def __repr__(self):
        return f"<{self.__class__.__name__}->: {self.reponame}"

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self


class GithubUserInfo(db.Model):
    __tablename__ = "github_users_info"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    last_update = db.Column(db.Date(), nullable=False)
    repositories = db.relationship(
        "GithubRepositories",
        secondary="gh_repos_and_gh_users",
        back_populates="contributors",
    )

    def __repr__(self):
        return f"<{self.__class__.__name__}->: {self.username}"

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @staticmethod
    def get_args(fields: str) -> dict:
        schema_args = {"many": True}
        if fields:
            schema_args["only"] = [
                field
                for field in fields.split(",")
                if field in GithubUserInfo.__table__.columns
            ]
        return schema_args

    @staticmethod
    def apply_order(query: BaseQuery, sort_keys: str) -> BaseQuery:
        if sort_keys:
            for key in sort_keys.split(","):
                desc = False
                if key.startswith("-"):
                    key = key[1:]
                    desc = True
                column_attr = getattr(GithubUserInfo, key, None)
                if column_attr is not None:
                    query = (
                        query.order_by(column_attr.desc())
                        if desc
                        else query.order_by(column_attr)
                    )
        return query

    @staticmethod
    def apply_filter(query: BaseQuery) -> BaseQuery:
        for param, value in request.args.items():
            if param not in {"fields", "sort", "page", "limit"}:
                if param == "username":
                    query = query.filter(GithubUserInfo.username.like(f"%{value}%"))
                    continue
                if param == "language":
                    langs_list = value.split(" ")
                    for lang in langs_list:
                        query = query.join(GithubUserInfo.repositories).filter(
                            GithubRepositories.languages.contains(lang)
                        )
                    continue
                if param.startswith("number_of_repositories"):
                    if param.endswith("[gt]"):
                        users_ids_list = []

                        subquery = (
                            query.join(GithubUserInfo.repositories)
                            .distinct(GithubUserInfo.id)
                            .all()
                        )

                        for user in subquery:
                            if len(user.repositories) > int(value):
                                users_ids_list.append(user.id)

                        query = query.filter(GithubUserInfo.id.in_(users_ids_list))

                        continue
                    elif param.endswith("[gte]"):
                        users_ids_list = []

                        subquery = (
                            query.join(GithubUserInfo.repositories)
                            .distinct(GithubUserInfo.id)
                            .all()
                        )

                        for user in subquery:
                            if len(user.repositories) >= int(value):
                                users_ids_list.append(user.id)

                        query = query.filter(GithubUserInfo.id.in_(users_ids_list))

                        continue
                    elif param.endswith("[lt]"):
                        users_ids_list = []

                        subquery = (
                            query.join(GithubUserInfo.repositories)
                            .distinct(GithubUserInfo.id)
                            .all()
                        )

                        for user in subquery:
                            if len(user.repositories) < int(value):
                                users_ids_list.append(user.id)

                        query = query.filter(GithubUserInfo.id.in_(users_ids_list))

                        continue
                    elif param.endswith("[lte]"):
                        users_ids_list = []

                        subquery = (
                            query.join(GithubUserInfo.repositories)
                            .distinct(GithubUserInfo.id)
                            .all()
                        )

                        for user in subquery:
                            if len(user.repositories) <= int(value):
                                users_ids_list.append(user.id)

                        query = query.filter(GithubUserInfo.id.in_(users_ids_list))

                        continue
                    else:
                        users_ids_list = []

                        subquery = (
                            query.join(GithubUserInfo.repositories)
                            .distinct(GithubUserInfo.id)
                            .all()
                        )

                        for user in subquery:
                            if len(user.repositories) == int(value):
                                users_ids_list.append(user.id)

                        query = query.filter(GithubUserInfo.id.in_(users_ids_list))

                        continue
                if param.startswith("date"):
                    pass
                    ## last_commit_date scraping functionality to be added to database

                    ## try:
                    ##     value = datetime.strptime(value, "%d-%m-%Y").date()
                    ##     if param.endswith("[gt]"):
                    ##         query = query.filter(GithubUserInfo.date > value)
                    ##         continue
                    ##     elif param.endswith("[gte]"):
                    ##         query = query.filter(GithubUserInfo.date >= value)
                    ##         continue
                    ##     elif param.endswith("[lt]"):
                    ##         query = query.filter(GithubUserInfo.date < value)
                    ##         continue
                    ##     elif param.endswith("[lte]"):
                    ##         query = query.filter(GithubUserInfo.date <= value)
                    ##         continue
                    ##     else:
                    ##         query = query.filter(GithubUserInfo.date == value)
                    ##         continue
                    ## except ValueError:
                    ##     continue
                if param.startswith("stars"):
                    if param.endswith("[gt]"):
                        users_ids_list = []
                        users_stars_dict = {}

                        subquery = (
                            query.join(GithubUserInfo.repositories)
                            .distinct(GithubUserInfo.id)
                            .all()
                        )

                        for user in subquery:
                            users_stars_dict[user] = 0
                            for repo in user.repositories:
                                users_stars_dict[user] = (
                                    users_stars_dict[user] + repo.stars
                                )
                            if users_stars_dict[user] > int(value):
                                users_ids_list.append(user.id)

                        query = query.filter(GithubUserInfo.id.in_(users_ids_list))
                        continue
                    elif param.endswith("[gte]"):
                        users_ids_list = []
                        users_stars_dict = {}

                        subquery = (
                            query.join(GithubUserInfo.repositories)
                            .distinct(GithubUserInfo.id)
                            .all()
                        )

                        for user in subquery:
                            users_stars_dict[user] = 0
                            for repo in user.repositories:
                                users_stars_dict[user] = (
                                    users_stars_dict[user] + repo.stars
                                )
                            if users_stars_dict[user] >= int(value):
                                users_ids_list.append(user.id)

                        query = query.filter(GithubUserInfo.id.in_(users_ids_list))
                        continue
                    elif param.endswith("[lt]"):
                        users_ids_list = []
                        users_stars_dict = {}

                        subquery = (
                            query.join(GithubUserInfo.repositories)
                            .distinct(GithubUserInfo.id)
                            .all()
                        )

                        for user in subquery:
                            users_stars_dict[user] = 0
                            for repo in user.repositories:
                                users_stars_dict[user] = (
                                    users_stars_dict[user] + repo.stars
                                )
                            if users_stars_dict[user] < int(value):
                                users_ids_list.append(user.id)

                        query = query.filter(GithubUserInfo.id.in_(users_ids_list))
                        continue
                    elif param.endswith("[lte]"):
                        users_ids_list = []
                        users_stars_dict = {}

                        subquery = (
                            query.join(GithubUserInfo.repositories)
                            .distinct(GithubUserInfo.id)
                            .all()
                        )

                        for user in subquery:
                            users_stars_dict[user] = 0
                            for repo in user.repositories:
                                users_stars_dict[user] = (
                                    users_stars_dict[user] + repo.stars
                                )
                            if users_stars_dict[user] <= int(value):
                                users_ids_list.append(user.id)

                        query = query.filter(GithubUserInfo.id.in_(users_ids_list))
                        continue
                    else:
                        users_ids_list = []
                        users_stars_dict = {}

                        subquery = (
                            query.join(GithubUserInfo.repositories)
                            .distinct(GithubUserInfo.id)
                            .all()
                        )

                        for user in subquery:
                            users_stars_dict[user] = 0
                            for repo in user.repositories:
                                users_stars_dict[user] = (
                                    users_stars_dict[user] + repo.stars
                                )
                            if users_stars_dict[user] == int(value):
                                users_ids_list.append(user.id)

                        query = query.filter(GithubUserInfo.id.in_(users_ids_list))
                        continue
                return query.all()

        return query

    @staticmethod
    def get_pagination(query: BaseQuery) -> Tuple[list, dict]:
        page = request.args.get("page", 1, type=int)
        limit = request.args.get(
            "limit", current_app.config.get("PER_PAGE", 5), type=int
        )
        params = {k: v for k, v in request.args.items() if k != "page"}
        paginate_object = query.paginate(page, limit, False)
        pagination = {
            "total_pages": paginate_object.pages,
            "total_records": paginate_object.total,
            "current_page": url_for(
                "api.users_api.get_users_info", page=page, **params
            ),
        }

        if paginate_object.has_next:
            pagination["next_page"] = url_for(
                "api.users_api.get_users_info", page=page + 1, **params
            )

        if paginate_object.has_prev:
            pagination["previous_page"] = url_for(
                "api.users_api.get_users_info", page=page - 1, **params
            )

        return paginate_object.items, pagination


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False, unique=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def generate_hashed_password(password=str) -> str:
        return generate_password_hash(password)

    def is_password_valid(self, password: str) -> bool:
        return check_password_hash(self.password, password)

    def generate_jwt(self) -> str:
        payload = {
            "user_id": self.id,
            "exp": datetime.utcnow()
            + timedelta(minutes=current_app.config.get("JWT_EXPIRED_MINUTES", 30)),
        }
        return jwt.encode(payload, current_app.config.get("SECRET_KEY"))


class GithubUserInfoSchema(Schema):
    """Serialization to json format"""

    id = fields.Integer(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(max=50))
    repository = fields.String(required=True, validate=validate.Length(max=70))
    languages = fields.List(fields.String(), required=True, type=str)
    date = fields.Date("%d-%m-%Y", required=True)
    stars = fields.Integer(required=True)
    number_of_repositories = fields.Integer(required=True)

    @validates("date")
    def validate_date(self, value):
        if value > datetime.now().date():
            raise ValidationError(f"Date must be earlier than {datetime.now().date()}")


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(max=250))
    email = fields.Email(required=True)
    password = fields.String(
        required=True, load_only=True, validate=validate.Length(min=4, max=250)
    )
    creation_date = fields.DateTime(dump_only=True)


class UserPasswordUpdateSchema(Schema):
    current_password = fields.String(
        required=True, load_only=True, validate=validate.Length(min=6, max=250)
    )
    new_password = fields.String(
        required=True, load_only=True, validate=validate.Length(min=6, max=250)
    )


info_schema = GithubUserInfoSchema()
user_schema = UserSchema()
user_password_update_schema = UserPasswordUpdateSchema()
