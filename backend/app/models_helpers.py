from random import seed, randint

import forgery_py
from sqlalchemy.exc import IntegrityError

from . import db
from .models import User, GithubUser


def create_fake_data(count):
    seed()
    for i in range(count):
        fake_user = User(email=forgery_py.internet.email_address(), active=True,)
        db.session.add(fake_user)

        fake_github_user = GithubUser(
            username=forgery_py.internet.user_name(True),
            repositories_count=randint(1, 3),
        )
        db.session.add(fake_github_user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
