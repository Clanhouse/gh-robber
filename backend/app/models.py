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
from sqlalchemy import or_
from sqlalchemy import and_
from sqlalchemy import not_
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.sql.expression import BinaryExpression
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from . import db


class GithubUserInfo(db.Model):
    __tablename__ = "github_users_info"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    repository = db.Column(db.String(70), nullable=False)
    languages = db.Column(db.JSON, nullable=False)
    date = db.Column(db.Date(), nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    number_of_repositories = db.Column(db.Integer, nullable=False)

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
                    query = query.filter(GithubUserInfo.language.like(f"%{value}%"))
                    continue
                if param.startswith('number_of_repositories'):
                    if param.endswith('[gt]'):
                        query = query.filter(GithubUserInfo.number_of_repositories > value)
                        continue
                    elif param.endswith('[gte]'):
                        query = query.filter(GithubUserInfo.number_of_repositories >= value)
                        continue
                    elif param.endswith('[lt]'):
                        query = query.filter(GithubUserInfo.number_of_repositories < value)
                        continue
                    elif param.endswith('[lte]'):
                        query = query.filter(GithubUserInfo.number_of_repositories <= value)
                        continue
                    else:
                        query = query.filter(GithubUserInfo.number_of_repositories == value)
                        continue
                if param.startswith("date"):
                    try:
                        value = datetime.strptime(value, '%d-%m-%Y').date()
                        if param.endswith('[gt]'):
                            query = query.filter(GithubUserInfo.date > value)
                            continue
                        elif param.endswith('[gte]'):
                            query = query.filter(GithubUserInfo.date >= value)
                            continue
                        elif param.endswith('[lt]'):
                            query = query.filter(GithubUserInfo.date < value)
                            continue
                        elif param.endswith('[lte]'):
                            query = query.filter(GithubUserInfo.date <= value)
                            continue
                        else:
                            query = query.filter(GithubUserInfo.date == value)
                            continue
                        continue
                    except ValueError:
                        continue
                if param.startswith('stars'):
                    if param.endswith('[gt]'):
                        query = query.filter(GithubUserInfo.stars > value)
                        continue
                    elif param.endswith('[gte]'):
                        query = query.filter(GithubUserInfo.stars >= value)
                        continue
                    elif param.endswith('[lt]'):
                        query = query.filter(GithubUserInfo.stars < value)
                        continue
                    elif param.endswith('[lte]'):
                        query = query.filter(GithubUserInfo.stars <= value)
                        continue
                    else:
                        query = query.filter(GithubUserInfo.stars == value)
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
