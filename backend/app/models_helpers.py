from random import choice, seed, randint
import random

import forgery_py
from sqlalchemy.exc import IntegrityError

from . import db
from .models import User, GithubUser, GithubUserInfo


LANGUAGE_LIST = ["JavaScript", "Java", "Python", "PHP", "C++", "C#", "TypeScript", "R", "Swift", "Kotlin", "Rust", "Julia"]

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



def create_fake_info(count=10):
    """Create sample data to database"""
    seed()
    for _ in range(count):
        fake_info = GithubUserInfo(
            username = forgery_py.internet.username(True),
            language = random.choice(LANGUAGE_LIST),
            date = forgery_py.date.day(),
            stars = randint(1, 100),
            number_of_repositories = randint(1, 10),
        )
        db.session.add(fake_info)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()