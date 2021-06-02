from . import db


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
