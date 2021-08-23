import re
from . import db
from marshmallow import Schema, fields, validate, validates,  ValidationError
from flask import request, url_for, current_app
from flask_sqlalchemy import BaseQuery
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.sql.expression import BinaryExpression
from typing import Tuple
from datetime import datetime
from backend.config import Config

COMPARISON_OPERATOR_RE = re.compile(r"(.*)\[(gte|gt|lte|lt)\]")


class GithubUserInfo(db.Model):
    __tablename__ = "github_users_info"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    language = db.Column(db.String(250), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    number_of_repositories = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<{self.__class__.__name__}>: {self.username}"

    def __init__(self, id, username, language, date, stars, number_of_repositories):
        self.id = id
        self.username = username
        self.language = language
        self.date = date
        self.stars = stars
        self.number_of_repositories = number_of_repositories

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @staticmethod
    def get_args(fields: str) -> dict:
        """
        Dynamically building arguments to the GithubUserInfoSchema class, returns json with the selected keys.
        key == fields
        value == id, username, language, date, stars, number_of_repositories
        example:  http://127.0.0.1:5000/api/v1.0/users/search?fields=id,username
        example:  http://127.0.0.1:5000/api/v1.0/users/search?fields=username,language
        """
        schema_args = {"many": True}
        if fields:
            schema_args["only"] = [field for field in fields.split(",") if field in GithubUserInfo.__table__.columns]
        return schema_args

    @staticmethod
    def apply_order(query: BaseQuery, sort_keys: str) -> BaseQuery:
        """
        Sort data in ascending or descending order
        key == sort
        value == id, username, language, date, stars, number_of_repositories
        sort ascending example:  http://127.0.0.1:5000/api/v1.0/users/search?sort=id,username
        sort descending example:  http://127.0.0.1:5000/api/v1.0/users/search?sort=-id,username
        """
        if sort_keys:
            for key in sort_keys.split(","):
                desc = False
                if key.startswith("-"):
                    key = key[1:]
                    desc = True
                column_attr = getattr(GithubUserInfo, key, None)
                if column_attr is not None:
                    query = query.order_by(column_attr.desc()) if desc() else query.order_by(column_attr)
        return query

    @staticmethod
    def get_filter_argument(column_name: InstrumentedAttribute, value: str, operator: str) -> BinaryExpression:
        operator_mapping = {
            "==": column_name == value,
            "gte": column_name >= value,
            "gt": column_name > value,
            "lte": column_name <= value,
            "lt": column_name < value
        }
        return operator_mapping[operator]

    @staticmethod
    def apply_filter(query: BaseQuery) -> BaseQuery:
        for param, value in request.args.items():
            if param not in {"fields", "sort", "page", "limit"}:
                operator = "=="
                match = COMPARISON_OPERATOR_RE.match(param)
                if match is not None:
                    param, operator = match.groups()
                column_attr = getattr(GithubUserInfo, param, None)
                if column_attr is not None:
                    if param == "date":
                        try:
                            value = datetime.strftime(value, "%d-%m-%Y").date()
                        except ValueError:
                            continue
                    filter_argument = GithubUserInfo.get_filter_argument(column_attr, value, operator)
                    query = query.filter(filter_argument)
        return query

    @staticmethod
    def get_pagination(query: BaseQuery) -> Tuple[list, dict]:
        page = request.args.get("page", 1, type=int)
        limit = request.args.get("limit", current_app.config.get("PER_PAGE", 5), type=int)
        params = {k: v for k, v in request.args.items() if k != "page"}
        paginate_object = query.paginate(page, limit, False)
        pagination = {
            "total_pages": paginate_object.pages,
            "total_records": paginate_object.total,
            "current_page": url_for("api.users_api.get_users_info", page=page, **params)
        }

        if paginate_object.has_next:
            pagination["next_page"] = url_for("api.users_api.get_users_info", page=page+1, **params)

        if paginate_object.has_prev:
            pagination["previous_page"] = url_for("api.users_api.get_users_info", page=page-1, **params)

        return paginate_object.items,  pagination


class GithubUserInfoSchema(Schema):

    class Meta:
        model = GithubUserInfo
        load_instance = True

    """Serialization to json format"""
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(max=50))
    language = fields.String(required=True, validate=validate.Length(max=250))
    date = fields.Date("%d-%m-%Y", required=True)
    stars = fields.Integer(required=True)
    number_of_repositories = fields.Integer(required=True)

    @validates("date")
    def validate_date(self, value):
        if value > datetime.now().date():
            raise ValidationError(f'Date must be earlier than {datetime.now().date()}')


info_schema = GithubUserInfoSchema()
