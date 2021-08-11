from . import db
from marshmallow import Schema, fields
from flask_sqlalchemy import BaseQuery
from datetime import date, datetime


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True)
    active = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<User {self.email}>"


class GithubUser(db.Model):
    __tablename__ = "github_users"
    username = db.Column(db.String(64), primary_key=True)
    repositories_count = db.Column(db.Integer)

    def __repr__(self):
        return f"<Github user {self.username}>"


class GithubUserInfo(db.Model):
    __tablename__ = "github_users_info"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    language = db.Column(db.String(250), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    stars = db.Column(db.Float(10), nullable=False)
    number_of_repositories = db.Column(db.Float(10), nullable=False)

    def __repr__(self):
        return f"<{self.__class__.__name__}>: {self.username}"

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


class GithubUserInfoSchema(Schema):
    """Serialization to json format"""
    id = fields.Integer()
    username = fields.String()
    language = fields.String()
    date = fields.Date("%d-%m-%Y")
    stars = fields.Float()
    number_of_repositories = fields.Float()


info_schema = GithubUserInfoSchema()
