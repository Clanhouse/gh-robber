from random import seed
from random import randint
from random import choice
import forgery_py
from sqlalchemy.exc import IntegrityError
from . import db
from app.models import GithubUserInfo, GithubRepositories
from app.models import GithubUserInfoSchema


LANGUAGE_LIST = [
    "JavaScript",
    "Java",
    "Python",
    "PHP",
    "C++",
    "C#",
    "TypeScript",
    "R",
    "Swift",
    "Kotlin",
    "Rust",
    "Julia",
]


def create_fake_info(count=10):
    """Create sample data to database"""
    seed()
    for _ in range(count):
        fake_repo = GithubRepositories(
            id=None,
            reponame=forgery_py.internet.user_name(True),
            languages=[choice(LANGUAGE_LIST)],
            topics=[1, 2, 3],
            last_update=forgery_py.date.date(),
            stars=randint(1, 100),
        )
        db.session.add(fake_repo)

        fake_user = GithubUserInfo(
            id=None,
            username=forgery_py.internet.user_name(True),
            repositories=[fake_repo],
        )
        db.session.add(fake_user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
